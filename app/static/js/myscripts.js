let page_ids = ["dashboard" , "categories", "manufacturer", "products", "orders"];
let page_data_cls = [".dash_stuff", ".cat_stuff", ".manu_stuff", ".prod_stuff", ".order_stuff"];

class Pages{
    constructor(page_id, page_data_cls){
        this.id = page_id;
        this.data_cls = page_data_cls;
    }
}

let objects = new Array(page_ids.length);

$(document).ready(function(){
    $('#sidebarCollapse').on('click', toggle_sidebar);
});

$(document).ready(toggle_sidebar);

$(document).ready(landing_view);

$(document).ready(function(){
    $("#dashboard").click(toggle_page_data);
    $("#categories").click(toggle_page_data);
    $("#manufacturer").click(toggle_page_data);
    $("#products").click(toggle_page_data);
    $("#orders").click(toggle_page_data);
});

function toggle_sidebar(){
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active');
}

function landing_view(){
    for(i = 0; i < page_ids.length; i+=1){
        objects[i] = new Pages(page_ids[i], page_data_cls[i]);
    }
    for(i = 0; i < objects.length; i+=1){
        if("dashboard" == objects[i].id){
            $(objects[i].data_cls).show();
        }
        else{
            $(objects[i].data_cls).hide();
        }
    }
}

function toggle_page_data(){
    let current_page = (this.id);
    for(i = 0; i < page_ids.length; i+=1){
        objects[i] = new Pages(page_ids[i], page_data_cls[i]);
    }
    for(i = 0; i < objects.length; i+=1){
        if(current_page == objects[i].id){
            $(objects[i].data_cls).show();
        }
        else{
            $(objects[i].data_cls).hide();
        }
    }
}
