<div class="left">
            <div class="top">
                <input type="text" />
                <a href="javascript:;" class="search"></a>
            </div>
            <ul class="people" style="overflow:scroll; height:500px;">
            	<?php for($i=0;$i<15;$i++){?>
                <li class="person" data-chat="person<?=$i;?>">
                    <img src="http://s13.postimg.org/ih41k9tqr/img1.jpg" alt="" />
                    <span class="name">Thomas Bangalter</span>
                    <span class="time">2:09 PM</span>
                    <span class="preview">I was wondering...</span>
                </li>
                <?php } ?>
            </ul>
        </div>