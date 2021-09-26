document.addEventListener("DOMContentLoaded", function (){

//  document.querySelector('footer').classList.remove('bg-secondary');
//  document.querySelector('footer').classList.add('navbar-default');


  document.querySelectorAll(".cat_btn").forEach(btn => {
    btn.onclick = function () {
      let cat = this.innerHTML

      document.querySelectorAll('.cat_head').forEach(c => {
        if (c.innerHTML == cat) {
          c.scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})
          c.style.animationPlayState = 'running';
        }
        setTimeout(function(){
          c.style.animationPlayState = 'paused';
        }, 5000)
      })
    }
  });

  // Scroll to Top

  //Get the button:
  mybutton = document.getElementById("topBtn");

  // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }

  // When the user clicks on the button, scroll to the top of the document
  mybutton.onclick = function() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  }

});