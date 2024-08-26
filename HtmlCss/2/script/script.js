function calc(){
    let first_number = parseInt(prompt("Введите первое число:"))
    let oper = prompt("Укажите операцию над числами (+, -, *, /")
    let second_number = parseInt(prompt("Введите второе число:"))
    switch(oper){
    case "+":
        alert(`${first_number} + ${second_number} = ${first_number+second_number}`)
        break;
    case "-":
        alert(`${first_number} - ${second_number} = ${first_number-second_number}`)
        break;
    case "*":
        alert(`${first_number} * ${second_number} = ${first_number*second_number}`)
        break; 
    case "/":
        if (second_number == 0) 
            alert('На ноль делить нельзя')
        else
            alert(`${first_number} / ${second_number} = ${first_number/second_number}`)
        break;
    default:
        alert("Операция не распознана.")    
    }
    
    
}