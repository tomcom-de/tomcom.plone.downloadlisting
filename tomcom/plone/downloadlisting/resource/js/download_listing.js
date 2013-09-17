var listing='1';

function handle_parent_click(element) {

    uid=$(element).attr('id').split('-')[1];

    var my_li = '#parent-'+uid;

    $('.parent-click').removeClass('current');
    $(element).addClass('current');

    if (!$('#span-'+uid).hasClass('open')) {
        open_tree(uid);
        $(my_li).css('background-image','url(icon_arrow_down.png)');
    } else {
        $(my_li).css('background-image','url(icon_arrow_right.png)');
        $('#span-'+uid).html('');
        $('#span-'+uid).removeClass('open');
        $('#content-'+uid).hide();

        var regex = /click-..../;
        currentClass=String(regex.exec($('#span-'+uid).attr('class')));
        $('#span-'+uid).removeClass(currentClass);
    }
}

function open_tree(uid) {

    dict_={}
    dict_['uid']=uid
    dict_['listing']=listing

    $.post('js_download_listing_level',
        dict_,
            function(data){
                $('#span-'+uid).html(data);
                $('#span-'+uid).addClass('open');
                $('#content-'+uid).show();

                var regex = /click-..../;
                currentClass=String(regex.exec($('#span-'+uid).attr('class')));
                if (!currentClass) {
                    $('#span-'+uid).addClass('click-'+clickCounter);
                    clickCounter=clickCounter+1;
                }
            }
    );
}

function handle_listing(element) {

    uid=$('.current-folder').attr('id').split('-')[1];

    dict_={}
    dict_['uid']=uid
    dict_['listing']=listing

    $.post('js_download-listing',
        dict_,
            function(data){
                $('#content-'+uid).html(data);
            }
    );
}

$( document ).ready(function() {

    $('body').delegate('.parent-click','click',function (event) {
        event.preventDefault();
        handle_parent_click(event.target);
    });

    $('body').delegate('#download-listing','click',function (event) {
        event.preventDefault();
        listing='1';
        handle_listing(event.target);
    });

    $('body').delegate('#download-gallery','click',function (event) {
        event.preventDefault();
        listing='2';
        handle_listing(event.target);
    });

});