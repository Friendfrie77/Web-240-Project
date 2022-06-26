jQuery(function() {
    jQuery('.job-image').click(function() {
      jQuery('#job' + $(this).attr('target')).slideToggle();
    });
  });