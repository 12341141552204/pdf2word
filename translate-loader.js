(function(){
  var s=document.createElement('style');
  s.textContent='.tm-tr{display:block;margin-top:4px;padding:2px 6px;background:#f0f7ff;border-left:3px solid #4a90d9;color:#333;font-size:0.9em;border-radius:2px}.tm-ld{color:#999;font-style:italic}';
  document.head.appendChild(s);

  function isEn(t){var m=t.match(/[a-zA-Z]/g);return m&&m.length/t.trim().length>0.3}
  function getDir(el){var t='';for(var c of el.childNodes)if(c.nodeType===3)t+=c.textContent;return t.trim()}
  function shouldTr(el){
    if(!el||!el.textContent)return false;
    if(el.hasAttribute('data-tm'))return false;
    if(el.classList.contains('tm-tr')||el.classList.contains('tm-ld'))return false;
    if(['SCRIPT','STYLE','INPUT','TEXTAREA'].includes(el.tagName))return false;
    var t=getDir(el);
    return t.length>=2&&t.length<=500&&isEn(t);
  }

  function tr(text,cb){
    var url='https://api.mymemory.translated.net/get?q='+encodeURIComponent(text)+'&langpair=en|zh-CN';
    fetch(url).then(function(r){return r.json()}).then(function(d){
      cb(d.responseData.translatedText||text);
    }).catch(function(){
      var url2='https://api.allorigins.win/raw?url='+encodeURIComponent('https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q='+encodeURIComponent(text));
      fetch(url2).then(function(r){return r.json()}).then(function(d){
        var t='';if(d&&d[0])for(var i=0;i<d[0].length;i++)if(d[0][i]&&d[0][i][0])t+=d[0][i][0];
        cb(t||text);
      }).catch(function(){cb(null)});
    });
  }

  if(window.__tmTranslated){
    document.querySelectorAll('.tm-tr,.tm-ld').forEach(function(e){e.remove()});
    document.querySelectorAll('[data-tm]').forEach(function(e){e.removeAttribute('data-tm')});
    window.__tmTranslated=false;
    return;
  }

  var els=document.querySelectorAll('p,h1,h2,h3,h4,h5,h6,li,td,th,figcaption,blockquote,label,a,span');
  var queue=[];
  els.forEach(function(el){
    if(shouldTr(el)){var t=getDir(el);if(t)queue.push({el:el,text:t})}
  });

  if(!queue.length){alert('没有找到需要翻译的英文内容');return}

  var done=0;
  queue.forEach(function(item,i){
    var ld=document.createElement('div');
    ld.className='tm-ld tm-tr';ld.textContent='正在翻译...';
    item.el.appendChild(ld);item.el.setAttribute('data-tm','1');
    setTimeout(function(){
      tr(item.text,function(res){
        ld.remove();
        if(res){var d=document.createElement('div');d.className='tm-tr';d.textContent='译文：'+res;item.el.appendChild(d)}
        done++;if(done===queue.length){window.__tmTranslated=true;console.log('翻译完成:'+done+'段')}
      });
    },i*200);
  });
  console.log('开始翻译'+queue.length+'段...');
})();
