//Makes the search button hinge
function noSearch(event) {
    event.preventDefault();
    var element = document.getElementById('hit-search-btn');
    element.classList.add('animate__hinge');
    setTimeout(
        function(){
            alert('Sorry, there is no search functionality right now :(')
        }, 2000
    )
}