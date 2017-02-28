 <div class="right">
            <div class="top"><span>To: <span class="name">Dog Woofson</span></span></div>
            <?php for($i=0; $i<10; $i++){ ?>
            <div class="chat" data-chat="person<?=$i;?>">
                <div class="conversation-start">
                    <span>Today, 6:48 AM</span>
                </div>
                <div class="bubble you">
                    Hello,
                </div>
                <div class="bubble you">
                    it's me.
                </div>
                <div class="bubble you">
                    I was wondering...
                </div>
            </div>
            <?php } ?>
            <div class="write">
                <a href="javascript:;" class="write-link attach"></a>
                <input type="text" />
                <a href="javascript:;" class="write-link smiley"></a>
                <a href="javascript:;" class="write-link send"></a>
            </div>
        </div>