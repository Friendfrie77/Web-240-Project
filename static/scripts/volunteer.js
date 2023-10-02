/* show and hide calander */
jQuery(function() {
    jQuery('.job-description').click(function() {
      jQuery('#job'+$(this).attr('target')).slideToggle();
    });
});
/* checking if checkbox is checked, if so displays email form */
jQuery(function() {
  jQuery('.paw-checkbox').click(function() {
    jQuery('#email'+$(this).attr('target')).slideToggle();
//   $(function(){
//     $(".txtEmail").prop('required',true);
//   });
  });
});

/* counter for hero */
document.addEventListener('DOMContentLoaded',function counters(){
  var counter = document.getElementById('counter');
  counter.innerText = '0';
  const updateCounter = () => {
    const target = +counter.getAttribute('data-target');
    const c = +counter.innerText
    const increment = target/500;
    if(c < target){
      counter.innerText= `${Math.ceil(c+increment)}`};
      setTimeout(updateCounter, 1);
  };
  updateCounter();
});

/* calander renders */
function showCalendar1() {
  var calendarEl = document.getElementById('calendar1');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventSources: [
      {
        url: '/cal1',
        method: 'GET',
        color: 'blue',
      }
    ]
  });
  calendar.render();
};
function showCalendar2() {
  var calendarEl = document.getElementById('calendar2');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventSources: [
      {
        
        url: '/cal2',
        method: 'GET',
        color: 'blue'
      }
    ]
  });
  calendar.render();
};
function showCalendar3() {
  var calendarEl = document.getElementById('calendar3');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventSources: [
      {
        
        url: '/cal3',
        method: 'GET',
        color: 'blue'
      }
    ]
  });
  calendar.render();
};
function showCalendar4() {
  var calendarEl = document.getElementById('calendar4');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventSources: [
      {
        
        url: '/cal4',
        method: 'GET',
        color: 'blue'
      }
    ]
  });
  calendar.render();
};
function showCalendar5() {
  var calendarEl = document.getElementById('calendar5');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventSources: [
      {
        url: '/cal5',
        method: 'GET',
        color: 'blue'
      }
    ]
  });
  calendar.render();
};
function showCalendar6() {
  var calendarEl = document.getElementById('calendar6');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventSources: [
      {
        url: '/cal6',
        method: 'GET',
        color: 'blue'
      }
    ]
  });
  calendar.render();
};

/*setting min and max date */
document.addEventListener('DOMContentLoaded', function(){
  let cd = new Date().toISOString().slice(0, 10)
  let fd = new Date()
  fd.setMonth( fd.getMonth() + 1 );
  fd = fd.toISOString().slice(0,10)
  const txtCal = document.getElementById('date')
  txtCal.setAttribute('max', fd)
  txtCal.setAttribute('min', cd)
});
