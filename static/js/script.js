function changeValue(id, delta) {
      const input = document.getElementById(id);
      let value = parseInt(input.value) || 0;
      value = Math.max(0, value + delta);
      input.value = value;
}

function clearTextboxUnitPrice() {
  document.getElementById("unit_price_modifier").value = "";
}

function setZeroDefaultUnitPrice() {
  const unitPriceModifier = document.getElementById("unit_price_modifier");
  if(unitPriceModifier.value.trim() === '')
    unitPriceModifier.value = '0';
}

function submitData() {
  const data = {
    has_cfo: document.getElementById('has_cfo').checked,
    has_burger_marketer: document.getElementById('has_burger_marketer').checked,
    has_pizza_marketer: document.getElementById('has_pizza_marketer').checked,
    has_drink_marketer: document.getElementById('has_drink_marketer').checked,
    has_firs_waitress_marketer: document.getElementById('has_firs_waitress_marketer').checked,
    burgers: parseInt(document.getElementById('burgers').value) || 0,
    pizzas: parseInt(document.getElementById('pizzas').value) || 0,
    drinks: parseInt(document.getElementById('drinks').value) || 0,
    waitress: parseInt(document.getElementById('waitress').value) || 0,
    salaries: parseInt(document.getElementById('salaries').value) || 0,
    unit_price_modifier: parseInt(document.getElementById('unit_price_modifier').value) || 0
  };

  const params = new URLSearchParams(data).toString();

  document.getElementById('burgers').value = 0
  document.getElementById('pizzas').value = 0
  document.getElementById('drinks').value = 0


  fetch(`/profit_calculator?${params}`)
    .then(response => response.json())
    .then(data => {
      Swal.fire({
        title: 'Profit Result',
        text: data['profit'] || "0",
        customClass: {
          htmlContainer: 'alert-text'
        },
        confirmButtonText: 'OK'
      });
    })
    .catch(error => {
      Swal.fire({
        title: 'Error',
        text: `Error: ${error}`,
        customClass: {
          htmlContainer: 'alert-text'
        },
        icon: 'error',
        confirmButtonText: 'Close'
    });
  });

}