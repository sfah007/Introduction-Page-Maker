let aElements = document.querySelectorAll('.social-media a');
window.onload = function(){
    aElements.forEach(function(el){
        el.classList.add('active');
    });
};