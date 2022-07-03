var cal1 = []
var cal2 = []
var cal3 = []
var cal4 = []
var cal5 = []
var cal6 = []

/* imports json for calendars */
// import('../json/test.json', {assert: {type: 'json'}}).then((mod)=>{
//   for (let i = 0; i < mod.default.length; i++){
//     let data = mod.default[i]
//     let test = Object.entries(data)
//     test = test.flat(1)
//     if (test[3] == "1"){
//       cal1.push(test)
//     }
//     if (test[3] == '2'){
//       cal2.push(test)
//     }
//     if (test[3] == "3"){
//       cal3.push(test)
//     }
//     if (test[3] == '4'){
//       cal4.push(test)
//     }
//     if (test[3] == "5"){
//       cal5.push(test)
//     }
//     if (test[3] == '6'){
//       cal6.push(test)
//     }
//   }  
// });
// console.log(cal1)
// console.log(cal2)
/* show and hide calander */
jQuery(function() {
    jQuery('.job-image').click(function() {
      jQuery('#job'+$(this).attr('target')).slideToggle();
    });
});

function ShowCalendar1() {
  var calendarEl = document.getElementById('calendar1');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventSources: [
      {
        
        url: '/cal1',
        method: 'GET',
        color: 'blue'
      }
    ]
  });
  calendar.render();
};
function ShowCalendar2() {
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
function ShowCalendar3() {
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
function ShowCalendar4() {
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
function ShowCalendar5() {
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
function ShowCalendar6() {
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

document.addEventListener('DOMContentLoaded', function(){
  let cd = new Date().toISOString().slice(0, 10)
  let fd = new Date()
  fd.setMonth( fd.getMonth() + 1 );
  fd = fd.toISOString().slice(0,10)
  const txtCal = document.getElementById('test')
  txtCal.setAttribute('max', fd)
  txtCal.setAttribute('min', cd)
});
