// Generated by CoffeeScript 1.4.0
(function() {
  var pathname;

  pathname = location.pathname;

  $(".nav>li").removeClass('active');

  $(".nav>li").each(function() {
    var self;
    self = $(this);
    if (self.children("a").attr('href') === pathname) {
      return self.addClass('active');
    }
  });

}).call(this);
