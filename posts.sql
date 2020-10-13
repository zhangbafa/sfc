/*
 Navicat Premium Data Transfer

 Source Server         : sfc
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 13/10/2020 17:52:30
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS "posts";
CREATE TABLE "posts" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "sender" varchar(20),
  "phone" integer(11),
  "content" TEXT,
  "createtime" integer(11),
  "type" integer(2) DEFAULT 1,
  "delete_time" integer DEFAULT 0
);

-- ----------------------------
-- Auto increment value for posts
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 290 WHERE name = 'posts';

-- ----------------------------
-- Indexes structure for table posts
-- ----------------------------
CREATE INDEX "createtime_type"
ON "posts" (
  "createtime" ASC,
  "type" ASC
);

PRAGMA foreign_keys = true;
