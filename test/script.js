document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('definition').addEventListener('keyup', function(e) {
        if (e.key === 'Enter') {
            console.log('Working!');
        }
    });
});

const newDefinition = document.createElement('input');
newDefinition.placeholder="Add a definition"
newDefinition.id="definition"
document.getElementById('definitions').appendChild(newDefinition);






const button = document.createElement('button');
button.onclick=createNewField("Add a definition","definition");
document.getElementById('frame').appendChild(button);