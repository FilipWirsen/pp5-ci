window.onscroll = function () { 
    scrollFunction();
    let scroll = this.scrollY;
    hide_header(scroll);
    document.getElementsByClassName('toast').toast('show');
};

    function scrollFunction() {
        var BackToTopBtn = document.getElementById("btn-back-to-top");
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            BackToTopBtn.style.display = "block";
        } else {
            BackToTopBtn.style.display = "none";
        }
    }

    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }

    function hide_header(scrollposition) {
        var MaxWidth = window.matchMedia("(max-width: 750px)");
        if (MaxWidth.matches) {
            var header = document.getElementById('header');
            if (scrollposition < 500) {
                header.classList.remove('d-none');
                header.classList.add('d-block');
            } else {
                header.classList.remove('d-block');
                header.classList.add('d-none');
            }
        }

    }