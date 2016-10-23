$(document).ready(function() {
  var protocol = 'https:';
  var text = 'HTTPS';
  var icon = 'plus';
  var link = $('#protocol > a');
  var glyph = $('#protocol > a > span.glyphicon');
  if (document.location.protocol === 'https:') {
    protocol = 'http:';
    text = 'HTTP';
    icon = 'minus';
  }
  link.append(text);
  glyph.addClass('glyphicon-' + icon + '-sign');
  link.click(function() {
    document.location.protocol = protocol;
    return false;
  });
});

