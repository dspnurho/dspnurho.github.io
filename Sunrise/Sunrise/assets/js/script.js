$(document).ready(function() {
	"use strict";
// --------------Newsletter-----------------------

	$(".newsletter-signup").ajaxChimp({
		callback: mailchimpResponse,
		url: "http://sandlabs.us9.list-manage.com/subscribe/post?u=a6801279da611bc55645c0413&id=9977eec545" // Replace your mailchimp post url inside double quote "".  
	});

	function mailchimpResponse(resp) {
		 if(resp.result === 'success') {
		 
			$('.alert-success').html(resp.msg).fadeIn().delay(3000).fadeOut();
			
		} else if(resp.result === 'error') {
			$('.alert-warning').html(resp.msg).fadeIn().delay(3000).fadeOut();
		}  
	};
 });