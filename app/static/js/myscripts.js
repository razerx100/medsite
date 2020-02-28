$(document).ready(function(){
    $('#sidebarCollapse').on('click', toggle_sidebar);
});

$(document).ready(toggle_sidebar);

$(document).ready(dashboard_show);

$(document).ready(function(){
    $('#dashboard').click(dashboard_show);
});

$(document).ready(function(){
    $('#categories').click(function(){
        $('.dash_stuff').hide();
        $('.cat_stuff').show();
    });
});

function toggle_sidebar(){
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active');
}

function dashboard_show(){
    $('.dash_stuff').show();
    $('.cat_stuff').hide();
}
