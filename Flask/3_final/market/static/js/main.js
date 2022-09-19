
/////////// 슬라이드 바 설정 /////////////
$(document).ready(function(){

    //메인에 들어가는 광고 슬라이더
    $('.slider').slick({
        slidesToShow: 1,
        autoplay:true,
        autoplaySpeed:5000,
        pauseOnHover:true,
        dots:true,
    });


    //메인 베스트셀러
    $('.slider-1').slick({
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 5000,
        pauseOnHover:true,
        dots:true,
    });

    //recipe_detail.html 추천재료 슬라이더
    $('.slider-recipe-recomm').slick({
        slidesToShow: 4,
        slidesToScroll: 4,
        autoplay: true,
        autoplaySpeed: 5000,
        pauseOnHover:true,
        dots:true,
    });

    //product_detail.html의 함께 산 제품 추천
    $('.pur-tog-recomm').slick({
        slidesToShow: 3, // 몇개 보일껀지
        slidesToScroll: 3, // 넘길때 몇개 넘어갈건지
        autoplay: true, //자동으로 play
        autoplaySpeed: 5000, //스피드
        pauseOnHover:true, //hover시 멈춤기능.
        dots:true,
    })

    //product_detail.html의 음식 들어간 레시피 추천
    $('.related-reci-recomm').slick({
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 5000,
        pauseOnHover:true,
        dots:true,
    })

    //cart.html의 추천제품
    $('.prod-recomm').slick({
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 5000,
        pauseOnHover:true,
        dots:true,
    })
});


//////////// 메뉴바 설정 //////////////
