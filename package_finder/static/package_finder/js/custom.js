document.addEventListener("DOMContentLoaded", function (){

  document.querySelectorAll(".cat_btn").forEach(btn => {
    btn.onclick = function () {
      let cat = this.innerHTML

      document.querySelectorAll('.cat_head').forEach(c => {
        if (c.innerHTML == cat) {
          c.style.animationPlayState = 'running';
        }
        setTimeout(function(){
          c.style.animationPlayState = 'paused';
        }, 5000)
      })
    }
  })
});