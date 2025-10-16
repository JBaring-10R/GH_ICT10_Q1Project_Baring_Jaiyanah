from pyscript import document # type: ignore

def compute_total(event=None):
    total = 0
    items = ["item1", "item2", "item3", "item4", "item5"]
    for item in items:
        checkbox = document.getElementById(item)
        if checkbox and checkbox.checked:
            total += int(checkbox.value)
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value
    summary = f"""
    <div class='info-box'>
        <b>Thank you for ordering, {name}!</b><br>
        Address: {address}<br>
        Contact No: {contact}<br>
        Total: ₱{total}
    </div>
    """
    document.getElementById("summary").innerHTML = summary

def clear_form(event=None):
    document.getElementById("orderForm").reset()
    document.getElementById("summary").innerHTML = ""