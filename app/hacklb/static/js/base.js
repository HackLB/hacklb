$( document ).ready(function() {
    console.log('Welcome to HackLB');
    setBreadcrumbMenu();
});

function setBreadcrumbMenu() {
	console.log('setBreadcrumbMenu');
	$("#menu-breadcrumb > li > a").each(function (index, value) { 
  		console.log(value); 
  		console.log($(this).attr('href')); 
  		console.log($(this).parent()); 

  		currentPath = window.location.pathname;
  		if ($(this).attr('href') == currentPath) {
  			$(this).parent().addClass('active');
  		} else {
  			$(this).parent().removeClass('active');
  		}

	});
}