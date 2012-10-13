var base_url			 = 'central';
var api_url				 = 'api';
var get_channel_messages = 'get-channel-messages';
var get_channel_users	 = 'get-channel-users';
var channel_name		 = '';

make_api_url = function(page, channel) {
	return ['', base_url, api_url, page, channel, ''].join('/');
}

pad = function (number, length) {

	var str = '' + number;
	while (str.length < length) {
		str = '0' + str;
	}

	return str;

}

generate_messages = function(data) {
	rows = [];
	$.each(data, function(key, value) {
		var row = $('<tr>');
		
		var user_cell = $('<td>').html(value['user'][0] + ':').addClass('user_cell');
		var message_cell = $('<td>').html(value['message']).addClass('message_cell');
		
		date_object = new Date(value['time_created']);
		date_string = pad(date_object.getHours() % 12, 2) + 'h ' + pad(date_object.getMinutes(), 2) + 'm ' + pad(date_object.getSeconds(), 2) + 's';
		
		var date_cell = $('<td>').html(date_string).addClass('date_cell');
		
		row.append(user_cell).append(message_cell).append(date_cell);
		rows.push(row);
	});
	
	return rows;
}

load_messages = function(url, element) {
	$.ajax({
		url: url,
		dataType: 'json',
		success: function(data) {
			rows = generate_messages(data);
			$.each(rows, function(key, value) {
				value.appendTo(element);
			});
		},
	});
}

load_users = function(url, element) {
	$.ajax({
		url: url,
		dataType: 'json',
		success: function(data) {
			$(element).html(data);
		},
	});
}

$(document).bind('reload', function(event) {
	load_messages(make_api_url(get_channel_messages, channel_name), 'table#chat_table');
	load_users(make_api_url(get_channel_users, channel_name), '.online_users');
});

$(document).ready(function () {
	channel_name = $('input[name="channel"]').val();
	
	$(document).triggerHandler('reload');
});