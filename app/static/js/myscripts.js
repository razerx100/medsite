class Link{
    constructor(id, data_cls){
        this.id = id;
        this.data_cls = data_cls;
    }
}

let idss = [["dashboard"] , ["categories"], ["manufacturer"], ["products"], ["orders"], ["add_cat_btn"]];
let data_clss = [".dash_stuff", ".cat_stuff", ".manu_stuff", ".prod_stuff", ".order_stuff", ".add_cat"];
let links = new Array(idss.length);

//Runs as soon as page finishes loading

$(document).ready(link_generator);

$(document).ready(function(){
    $('#sidebarCollapse').on('click', on_click_toggle);
    for (ids of idss){
        for (id of ids){
            let a_id = "#" + id;
            $(a_id).on('click', on_click_toggle);
        }
    }
});

function toggle_sidebar(){
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active');
}

function link_generator(){
    for(i = 0; i < idss.length; i++){
        links[i] = new Link(idss[i], data_clss[i]);
    }
}

function finding_class(current_page){
    for(i = 0; i < links.length; i++){
        for(j = 0; j < links[i].id.length; j++){
            if(links[i].id[j] == current_page){
                return links[i].data_cls;
            }
        }
    }
}

function toggle_view(data_class){
    for(i = 0; i < data_clss.length; i++){
        if(data_clss[i] == data_class){
            $(data_clss[i]).show();
        }
        else{
            $(data_clss[i]).hide();
        }
    }
}

function on_click_toggle(){
    let current_page_id = this.id;
    toggle_view(finding_class(current_page_id));
}
