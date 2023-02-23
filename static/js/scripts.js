/* Локализация datepicker */
$.datepicker.regional['ru'] = {
closeText: 'Закрыть',
prevText: 'Предыдущий',
nextText: 'Следующий',
currentText: 'Сегодня',
monthNames: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
monthNamesShort: ['Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Ноя','Дек'],
dayNames: ['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота'],
dayNamesShort: ['вск','пнд','втр','срд','чтв','птн','сбт'],
dayNamesMin: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'],
weekHeader: 'Не',
dateFormat: 'dd.mm.yy',
firstDay: 1,
isRTL: false,
showMonthAfterYear: false,
yearSuffix: ''
};
$.datepicker.setDefaults($.datepicker.regional['ru']);
/* Локализация datepicker */


/* <add_kitchen */
//Функционал, при нажатий кнопки 'Кухонный гарнитур'
function press_add_kitchen_btn(reckoning_uuid){
    var the_btn = $('#addkitchenbtn_'+reckoning_uuid);
    var kitchen_count = the_btn.attr('kitchen_count');
    var add_comment_block = $('#add_kitchen_offerpage_'+reckoning_uuid);
    var comments_block = $('#kitchen_offerpages_'+reckoning_uuid);
    if (the_btn.attr('showed') == '0') {
        the_btn.html('<span class="glyphicon glyphicon-comment" aria-hidden="true"></span> Закрыть вкладку ('+kitchen_count+')');
        the_btn.attr('showed', '1');
        the_btn.addClass('btn-default');
        the_btn.removeClass('btn-success');
        load_add_kitchen_offerpage_form(reckoning_uuid);
        load_kitchen_offerpages(reckoning_uuid);
    } else {
        the_btn.html('<span class="glyphicon glyphicon-comment" aria-hidden="true"></span> Кухонный гарнитур ('+kitchen_count+')');
        the_btn.attr('showed', '0');
        the_btn.removeClass('btn-default');
        the_btn.addClass('btn-success');
        add_comment_block.html('');
		comments_block.html('');
    }
}
$(document).ready(function() {
	if ( $('.add_kitchen_btn').length ) {
		var kitchen_offerpage_count = $('.add_kitchen_btn').attr('kitchen_count');
		if ( kitchen_offerpage_count > 0 ) {
			var reckoning_uuid = $('.add_kitchen_btn').attr('reckoninguuid');
			press_add_kitchen_btn(reckoning_uuid);
		}
	}
});
//Загрузить форму для кухонного гарнитура
function load_add_kitchen_offerpage_form(reckoning_uuid){
    var add_kitchen_offerpage_block = $("#add_kitchen_offerpage_"+reckoning_uuid);
    $.ajax({
        type: "GET",
        url: "/presentation/"+reckoning_uuid+"/add_kitchen_offer_page",
        data: "",
		success: function(data) {
			add_kitchen_offerpage_block.html(data);
		}
    });
}
//Выгрузить список КП для кухонных гарнитуров
function load_kitchen_offerpages(reckoning_uuid){
	var comments_block = $("#kitchen_offerpages_"+reckoning_uuid);
	var the_btn = $("#addkitchenbtn_"+reckoning_uuid);
	if(the_btn.attr("showed") == "1"){
		$.ajax({
			type: "GET",
			url: "/presentation/"+reckoning_uuid+"/kitchen_offerpages_list",
			data: "",
			success: function(data) {
				comments_block.html(data);
			}
		});
	}
}

//Добавить новый позицию для КП
function add_new_kitchen_offerpages(reckoning_uuid, csrfmiddlewaretoken){
	var comments_block = $("#kitchen_offerpages_"+reckoning_uuid);
	var upperfacades = encodeURIComponent($("#id_upperfacades_"+reckoning_uuid).val());
	var lowerfacades = encodeURIComponent($("#id_lowerfacades_"+reckoning_uuid).val());
	var tabletop = encodeURIComponent($("#id_tabletop_"+reckoning_uuid).val());
	var other = encodeURIComponent($("#id_other_"+reckoning_uuid).val());
	var accessories = encodeURIComponent($("#id_accessories_"+reckoning_uuid).val());
	var sketch = encodeURIComponent($("#id_sketch_"+reckoning_uuid).val());
	var costcalculation = encodeURIComponent($("#id_costcalculation_"+reckoning_uuid).val());
	var total_price = encodeURIComponent($("#id_total_price_"+reckoning_uuid).val());
	var total_discounted_price = encodeURIComponent($("#id_total_discounted_price_"+reckoning_uuid).val());
	$.ajax({
		type: "POST",
		url: "/presentation/"+reckoning_uuid+"/kitchen_offerpages_list",
		data: "csrfmiddlewaretoken="+csrfmiddlewaretoken+"&upperfacades="+upperfacades+"&lowerfacades="+lowerfacades+"&tabletop="+tabletop+"&other="+other+"&accessories="+accessories+"&sketch="+sketch+"&costcalculation="+costcalculation+"&total_price="+total_price+"&total_discounted_price="+total_discounted_price,
		success: function(data) {
			comments_block.html(data);
			load_add_kitchen_offerpage_form(reckoning_uuid);
			update_kitchen_offerpages_count(reckoning_uuid);
		}
	});
}
function update_kitchen_offerpages_count(reckoning_uuid){
	var the_btn = $("#addkitchenbtn_"+reckoning_uuid);
	if(the_btn.attr("showed") == "1"){
		$.ajax({
			type: "GET",
			url: "/presentation/"+reckoning_uuid+"/kitchen_count",
			data: "",
			success: function(data) {
				the_btn.html('<span class="glyphicon glyphicon-comment" aria-hidden="true"></span> Закрыть ('+data+')');
				the_btn.attr('kitchen_count', data);
			}
		});
	}
}
/* <add_kitchen */