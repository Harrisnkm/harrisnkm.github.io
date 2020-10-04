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

//active
function setActivePage() {
    //get the url of page
    let urlPath = window.location.href

    //get the page from the url
    let currentPage = urlPath.substring(urlPath.lastIndexOf('/') + 1) || 'index.html'


    //find the href with this page inside the nav class
    let currentPageLink = document.querySelectorAll("a[href='"+currentPage+"']")[0]

    console.log(currentPageLink)
    //adds the #activeNavLink to element
    currentPageLink.setAttribute('id','activeNavLink')

    return currentPage
}