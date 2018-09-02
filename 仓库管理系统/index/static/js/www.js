function addRow(){
                //添加一行
                var newTr = tb.insertRow();
                //添加3列
                var newTd0 = newTr.insertCell();
                var newTd1 = newTr.insertCell();
                var newTd2 = newTr.insertCell();
                var i=document.getElementsByTagName('tr').length-2
                //设置列内容和属性
                newTd0.innerHTML = '<input type="text" name="ushpmc'+i+'" maxlength="50">';
                newTd1.innerHTML = '<input type="text" name="ushpshl'+i+'" maxlength="6">';
                newTd2.innerHTML = '<input type="text" name="ushpjg'+i+'" maxlength="6">';
            }