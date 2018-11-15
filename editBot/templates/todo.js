var ul=document.getElementById('list')
var br=document.getElementById('br')
var li;


var addButton = document.getElementById('add')
addButton.addEventListener('click',addItem)

var removeButton = document.getElementById('remove')
removeButton.addEventListener('click',removeItem)

var removeAllButton = document.getElementById('removeall')
removeAllButton.addEventListener('click',removeAllItem)



function addItem(){
    var input = document.getElementById('input')
    var item=input.value;
    var textnode = document.createTextNode(item)
    
    if(item === ''){
        var pTag=document.createElement("p")
        pTag.textContent="Enter Your Task"
        console.log(pTag)
        br.insertBefore(pTag,br.childNodes[0]) 
//        pTag.className='.visual'
        //document.querySelector('body').appendChild(myNewPara)
        return false
    }else{
        li=document.createElement('li');
        var checkbox =  document.createElement('input');
        checkbox.type='checkbox';
        checkbox.setAttribute('id','check');
        var label= document.createElement('label');
        label.setAttribute('for','item')
        
        //add the element to ul
        ul.appendChild(label);
        li.appendChild(checkbox);
        label.appendChild(textnode);
        li.appendChild(label);
        ul.insertBefore(li,ul.childNodes[0])
        li.className='visual'
        
        input.value = ''
    }
}

function removeItem(){
    li =  ul.children
//    console.log(li)
    for(let index=0; index<li.length;index++){
        while(li[index] && li[index].children[0].checked){
            ul.removeChild(li[index])
        }
        
    }
}

function removeAllItem(){
//    for(let index=0; index<li.length;index++){
//        ul.removeChild(li[index])
//    }
    while(ul.firstChild)
        ul.removeChild(ul.firstChild)
}