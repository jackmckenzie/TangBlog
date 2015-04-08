
(function($){
	$('#polls-form').entwine({
		vote: function() {
			console.log($("#qid").val());
			$.ajax({
				url: "/polls/vote/",
				type: "POST",
				data: {
					'csrfmiddlewaretoken' : $('[name="csrfmiddlewaretoken"]').val(),
				'the_vote': $("#vote-choice input:checked").val(),
				'question_id': $("#qid").val()
				},
				success : function(json) {
					text = '';
					$.each(json, function() {
						text += "<li>" + this['fields']['choice_text'] + ": " + this['fields']['votes'] + "</li>";
					});
					$('ul#result').html(text);
				},
				error : function(xhr,errmsg,err) {
					$("#results-msg").html('<div class="alert-box" data-alert="Oops! Error time ' + errmsg + ' <a href="#" class="close">&times;</a></div>');
					console.log(xhr.status, + ": " + xhr.responseText);
				}
			});
		},
		onmatch: function() {
			this.vote();
		},
		onsubmit: function(event) {
			event.preventDefault();
			this.vote();
		}
	})
})(jQuery);

