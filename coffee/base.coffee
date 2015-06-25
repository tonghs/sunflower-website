$.fn.extend(
    parallax: ->
        scroll_top = $(window).scrollTop()
        self = $(this)
        ratio = parseFloat(self.data('parallax-background-ratio'))
        self.css('background-position', "0 #{scroll_top * ratio}px")
)
