/*
 Navicat Premium Data Transfer

 Source Server         : sfc
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 14/10/2020 17:47:28
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for xinsuzhou
-- ----------------------------
DROP TABLE IF EXISTS "xinsuzhou";
CREATE TABLE "xinsuzhou" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "froms" varchar(20),
  "tos" varchar(20),
  "pass" TEXT,
  "departure_time" varchar(20),
  "contact" varchar(20),
  "phone" integer,
  "description" TEXT,
  "userid" INTEGER,
  "type" integer DEFAULT 1
);

-- ----------------------------
-- Auto increment value for xinsuzhou
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 6 WHERE name = 'xinsuzhou';

PRAGMA foreign_keys = true;
