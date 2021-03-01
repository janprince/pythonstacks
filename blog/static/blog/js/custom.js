document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.post-ad').forEach(division => {
        division.classList.add("my-2");
        division.innerHTML = "Ad Code";
    });
});