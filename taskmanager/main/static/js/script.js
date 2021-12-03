function Board(){
    var square;
    var container = document.getElementById('container');
    for (var i; i < 9; i++){
        for (var k; k < 9: k++){
            square = createElement('div');
            if ((i + j) % 2 != 0){
                square.style.backgroundColor = 'white';
            }
            else{
                square.style.backgroundColor = 'black';
            }
            square.classList.add('square');
            container.appendChild(square);
        }
    }
}


function CreateTable(){
    var poz = document.getElementById('space');

    // createing table adn inserting into document
    tab = document.createElement('table');
    poz.appendChild(tab);

    tab.border = '5';

    for (var i = 0; i < 8; i++){
        // creating row and inserting into document
        var row = tab.insertRow(i);

        for(var j = 0; j < 8; j++){
            // creating cells and fill with data (numbers)
            var cell = row.insertCell(j);
            cell.innerHTML = i*j;
            cell.style.backgroundColor = 'blue';
            cell.style.color = 'white';
            cell.style.height = '50px';
            cell.style.width = '50px';

        };
    };

}