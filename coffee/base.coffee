$.fn.extend(
    parallax: ->
        scroll_top = $(window).scrollTop()
        self = $(this)
        ratio = parseFloat(self.data('parallax-background-ratio'))
        self.css('background-position', "center #{scroll_top * ratio}px")
)

$('.to-top').click ->
    $("html,body").animate({scrollTop: $("#top").offset().top - 60}, 500)

$(window).scroll ->
    # $('#home').parallax()
    # scroll_top = $(window).scrollTop()

    # if scroll_top > 0
    #     $('.to-top').css('opacity', 1)
    # else
    #     $('.to-top').css('opacity', '0')

$("#footer-sns #weixin").poshytip({
    className: 'tip-twitter',
    alignTo: 'target',
    alignX: 'center',
})


pathname = location.pathname
$("#navbar>ul>li").removeClass('active')
$("#navbar>ul>li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')

window.def_view = (module, ctrl, fun)->
    app = angular.module(module, ["ngSanitize"]).controller ctrl, fun

    app.filter('deal_str', ->
        return $.deal_str
    )

    return app


$(".nav>li").removeClass('active')
$(".nav>li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')

$('.table-expandable>tbody>tr>td>a.open').click ->
    obj = $(this).parent('td').parent('tr').next()
    if obj.attr('class') and obj.attr('class').indexOf('collapse') >= 0
        if obj.css('display') == 'none'
            obj.slideDown()
        else
            obj.slideUp(0)



$.postJSON = (url, data, callback) ->
    $.ajax(
        url: url,
        data: data,
        type: 'post',
        success: callback
    )

$.deal_str = (str)->
    r = new RegExp('>', 'g')
    str = str.replace(r, '&gt;')

    r = new RegExp('<', 'g')
    str = str.replace(r, '&lt;')
   
    str = str.replace(/\n/g, "</p><p>")

    return "<p>#{str}</p>"

$.alert =->
    dialog = BootstrapDialog.show({
        title: '提示',
        message: '保存成功'
        buttons: [{
            label: '关闭',
            action: (dialogItself)->
                dialogItself.close()
        }]
    })
    
    setTimeout(->
        dialog.close()
    , 2000)

