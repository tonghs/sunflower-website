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

  $('.table-expandable>tbody>tr>td>a.open').click(function() {
    var obj;
    obj = $(this).parent('td').parent('tr').next();
    if (obj.attr('class') && obj.attr('class').indexOf('collapse') >= 0) {
      if (obj.css('display') === 'none') {
        return obj.slideDown();
      } else {
        return obj.slideUp(0);
      }
    }
  });

}).call(this);
