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


///* <add_kitchen */
////Функционал, при нажатий кнопки 'Кухонный гарнитур'
//function press_add_kitchen_btn(reckoning_uuid){
//    var the_btn = $('#addkitchenbtn_'+reckoning_uuid);
//    var kitchen_count = the_btn.attr('kitchen_count');
//    var add_comment_block = $('#add_kitchen_offerpage_'+reckoning_uuid);
//    var comments_block = $('#kitchen_offerpages_'+reckoning_uuid);
//    if (the_btn.attr('showed') == '0') {
//        the_btn.html('<span class="glyphicon glyphicon-comment" aria-hidden="true"></span> Закрыть ('+kitchen_count+')');
//        the_btn.attr('showed', '1');
//        the_btn.addClass('btn-default');
//        the_btn.removeClass('btn-success');
//        load_add_kitchen_offerpage_form(reckoning_uuid);
//        load_kitchen_offerpages(reckoning_uuid);
//    } else {
//        the_btn.html('<span class="glyphicon glyphicon-comment" aria-hidden="true"></span> Добавить ('+kitchen_count+')');
//        the_btn.attr('showed', '0');
//        the_btn.removeClass('btn-default');
//        the_btn.addClass('btn-success');
//        add_comment_block.html('');
//		comments_block.html('');
//    }
//}
//$(document).ready(function() {
//	if ( $('.add_kitchen_btn').length ) {
//		var comments_count = $('.add_kitchen_btn').attr('kitchen_count');
//		if ( comments_count > 0 ) {
//			var froze_uuid = $('.add_kitchen_btn').attr('kitchen_count');
//			press_add_kitchen_btn(reckoning_uuid);
//		}
//	}
//});
////Загрузить форму для кухонного гарнитура
//function load_add_kitchen_offerpage_form(reckoning_uuid){
//    var add_kitchen_offerpage_block = $("#add_kitchen_offerpage_"+reckoning_uuid);
//    $.ajax({
//        type: "GET",
//        url: "/presentation/"+reckoning_uuid+"/add_kitchen_offer_page",
//        data: "",
//		success: function(data) {
//			add_comment_block.html(data);
//		}
//    });
//}
////Выгрузить список КП для кухонных гарнитуров
//function load_kitchen_offerpages(reckoning_uuid){
//	var comments_block = $("#kitchen_offerpages_"+reckoning_uuid);
//	var the_btn = $("#addkitchenbtn_"+reckoning_uuid);
//	if(the_btn.attr("showed") == "1"){
//		$.ajax({
//			type: "GET",
//			url: "/presentation/"+reckoning_uuid+"/kitchen_offerpages_list",
//			data: "",
//			success: function(data) {
//				comments_block.html(data);
//			}
//		});
//	}
//}
//
////Добавить новый комментарии
//function add_new_kitchen_offerpages(reckoning_uuid, csrfmiddlewaretoken){
//	var comments_block = $("#kitchen_offerpages_"+reckoning_uuid);
//	var content = encodeURIComponent($("#id_content_"+froze_uuid).val());
//	var date_check = encodeURIComponent($("#id_date_check_"+froze_uuid).val());
//	var status = encodeURIComponent($("#id_status_"+froze_uuid).val());
//	$.ajax({
//		type: "POST",
//		url: "/comments/"+froze_uuid+"/chief_comments_list",
//		data: "csrfmiddlewaretoken="+csrfmiddlewaretoken+"&content="+content+"&date_check="+date_check+"&status="+status,
//		success: function(data) {
//			comments_block.html(data);
//			load_add_chief_comment_form(froze_uuid);
//			update_chiefbtn_count(froze_uuid);
//		}
//	});
//}