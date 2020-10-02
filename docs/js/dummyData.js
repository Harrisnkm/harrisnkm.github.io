function createBlogs(numOfBlogs){
    var allBlogs = ""

    const loremText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ipsum. Aliquam volutpat orci diam, non gravida libero lit. Nunc ipsum. Aliquam volutpat orci diam, non gravida libero lit. Nunc ipsum. Aliquam volutpat orci diam, non gravida libero lit. Nunc ipsum. Aliquam volutpat orci diam, non gravida libero lit. Nunc ipsum. Aliquam volutpat orci diam, non gravida libero lit. Nunc ipsum. Aliquam volutpat orci diam, non gravida libero  dignissim eu. Pellentesque sit amet volutpat dui. Fusce varius sed ligula non convallis. In eu dictum risus, at lobortis enim. Praesent faucibus quam quis ligula varius, non ullamcorper diam convallis. Sed ut nulla leo. Nunc dignissim, dui ut aliquet fermentum, turpis lectus laoreet orci, non commodo nisi est quis neque. Maecenas suscipit libero nec purus sollicitudin, faucibus semper tortor molestie. Donec aliquet elit vel justo venenatis sodales. Mauris tempus est est, id condimentum massa ultrices et. Vivamus condimentum eget arcu eget viverra. Ut dictum felis et arcu tempor convallis. Nunc venenatis rutrum ante, in fringilla mi tempor et. Nunc varius massa vel sollicitudin imperdiet. In ac malesuada lectus. Morbi dui sapien, convallis vitae facilisis ut, maximus quis ante. Nulla semper eros eget eros cursus, nec eleifend odio vestibulum. Quisque commodo metus ac auctor dignissim. Pellentesque blandit turpis quis enim varius rhoncus. Etiam sed fringilla purus, vestibulum efficitur nisi. Proin mi sem, luctus ut urna fringilla, ultricies ullamcorper quam. Nam egestas lacinia orci, id dapibus diam accumsan quis. Nullam arcu odio, mollis in nulla aliquet, euismod dictum ipsum. Fusce lobortis magna et diam ornare sollicitudin ut vitae ligula."
    const author = "Harry"

    var x = 1
    var y = numOfBlogs

    while (x < y) {
        allBlogs += `<div class="card mb-5" style="height:400px; overflow: hidden;">
                      <div class="row no-gutters">
                        <div class="col-auto">
                            <img class="img-fluid" src="https://source.unsplash.com/random/400x400?sig=${x}">
                        </div>
                      
                      <div class="col">
                          <div class="card-block p-5">
                            <h5 class="card-title" >Title ${x}</h5>
                            <p class="card-text" style="height: 250px; overflow: hidden; margin-bottom: 20px;">${loremText}</p>
                            <a href="#" class="btn btn-primary">Read More...</a>
                          </div>
                      </div>
                      </div>
                      
                    </div>`

        x++
    }

    return allBlogs;

}





