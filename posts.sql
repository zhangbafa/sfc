CREATE TABLE "posts" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "sender" varchar(20) COMMENT '发布人',
  "phone" varchar(11) COMMENT '手机号码', 
  "content" TEXT COMMENT '发布内容',
  "createtime" varchar(11) COMMENT '发布时间',
  "type" integer(1) DEFAULT 1 COMMENT '车找人（1），人找车（0）' 
);