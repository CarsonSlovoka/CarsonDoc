/*
Reference:
    - http://jsfiddle.net/BB3JK/47/
    - https://codepen.io/wallaceerick/pen/ctsCz
*/

$('select').each(function(){ // find all node of "select"
    var $this = $(this), numberOfOptions = $(this).children('option').length;
  
    $this.addClass('select-hidden');
    $this.wrap('<div class="select"></div>');  // this div will wrap "this"
    $this.after('<div class="select-styled"></div>'); 

    var $styledSelect = $this.next('div.select-styled');
    $styledSelect.text($this.children('option').eq(0).text());
  
    var $list = $('<ul />', {
        'class': 'select-options'
    }).insertAfter($styledSelect);
  
    for (var i = 0; i < numberOfOptions; i++) {
        $('<li />', {
            text: $this.children('option').eq(i).text(),
            rel: $this.children('option').eq(i).val()
        }).appendTo($list);
    }
  
    var $listItems = $list.children('li');
  
    $styledSelect.click(function(e) {
        e.stopPropagation();
        $('div.select-styled.active').not(this).each(function(){
            $(this).removeClass('active').next('ul.select-options').hide();
        });
        $(this).toggleClass('active').next('ul.select-options').toggle();		
    });
  
    $listItems.click(function(e) {
        e.stopPropagation();
        $styledSelect.text($(this).text()).removeClass('active');
        $this.val($(this).attr('rel'));
        $list.hide();        
		window.location.href = $this.val(); // link to select language page
		//console.log($this.val());
    });
  
    $(document).click(function() {
        $styledSelect.removeClass('active');
        $list.hide();
    });
		

});