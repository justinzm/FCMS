/*
 Navicat Premium Data Transfer

 Source Server         : 本机
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : tp5cms

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 10/04/2022 08:41:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for club_ad
-- ----------------------------
DROP TABLE IF EXISTS `club_ad`;
CREATE TABLE `club_ad`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '广告ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '广告标题',
  `url` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '广告链接地址',
  `img` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '广告图片',
  `intro` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '广告代码',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '类型',
  `hits` int(11) NULL DEFAULT NULL COMMENT '点击量',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for club_article
-- ----------------------------
DROP TABLE IF EXISTS `club_article`;
CREATE TABLE `club_article`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '文章标题',
  `alias` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '文章别名',
  `metakeys` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'SEO关键词',
  `metadesc` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'SEO描述',
  `intro` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '简介',
  `img` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '文章图片',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '正文',
  `istop` tinyint(1) NULL DEFAULT NULL COMMENT '是否置顶',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `author` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '来源/作者',
  `hits` int(11) NULL DEFAULT NULL COMMENT '点击量',
  `praise` int(11) NULL DEFAULT NULL COMMENT '点赞量',
  `start_time` int(11) NULL DEFAULT NULL COMMENT '开始时间',
  `end_time` int(11) NULL DEFAULT NULL COMMENT '截止时间',
  `category_id` int(11) NULL DEFAULT NULL,
  `section_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `category_id`(`category_id`) USING BTREE,
  INDEX `section_id`(`section_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for club_auth_group
-- ----------------------------
DROP TABLE IF EXISTS `club_auth_group`;
CREATE TABLE `club_auth_group`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限组ID',
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '权限组名称',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `permissions` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '规则列表',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of club_auth_group
-- ----------------------------
INSERT INTO `club_auth_group` VALUES (0, 1550215694, 1639474228, NULL, 1, '系统管理员', 1, '1,2,3,4,5,6,7,8,9,15,10,11,12,13,14,16,18,50,51,52,53,54,55,56,57,19,20,23,24,25,21,26,27,28,22,29,30,31,58,59,60,61,45,46,47,48,49');
INSERT INTO `club_auth_group` VALUES (0, 1550215702, 1639298347, NULL, 2, '普通管理员', 1, '1,2');

-- ----------------------------
-- Table structure for club_auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `club_auth_permission`;
CREATE TABLE `club_auth_permission`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限规则ID',
  `per_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '规则名称（控制器）',
  `per_title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '菜单名称',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `icon` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '图标',
  `pid` int(11) NULL DEFAULT NULL COMMENT '父级ID',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 62 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of club_auth_permission
-- ----------------------------
INSERT INTO `club_auth_permission` VALUES (0, 1550240302, 1639372139, NULL, 1, '', '管理员管理', 1, 'user', 0, 7);
INSERT INTO `club_auth_permission` VALUES (0, 1550240334, NULL, NULL, 2, '/admin/auth_user/index', '管理员管理', 1, '', 1, 5);
INSERT INTO `club_auth_permission` VALUES (0, 1550240396, NULL, NULL, 3, '/admin/auth_user/add', '添加管理员', 1, '', 2, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550240466, NULL, NULL, 4, '/admin/auth_user/edit', '修改管理员', 1, '', 2, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550240489, NULL, NULL, 5, '/admin/auth_user/delete', '删除管理员', 1, '', 2, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550240552, NULL, NULL, 6, '/admin/auth_group/index', '权限组管理', 1, '', 1, 3);
INSERT INTO `club_auth_permission` VALUES (0, 1550240612, NULL, NULL, 7, '/admin/auth_group/add', '添加权限组', 1, '', 6, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550240670, NULL, NULL, 8, '/admin/auth_group/edit', '修改权限组', 1, '', 6, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550240708, NULL, NULL, 9, '/admin/auth_group/delete', '删除权限组', 1, '', 6, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550240884, 1639372178, NULL, 10, '', '站点管理', 1, 'home', 0, 5);
INSERT INTO `club_auth_permission` VALUES (0, 1550240926, NULL, NULL, 11, '/admin/auth_permission/index', '菜单(权限)管理', 1, '', 10, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550243521, NULL, NULL, 12, '/admin/auth_permission/add', '添加菜单', 1, '', 11, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550243703, NULL, NULL, 13, '/admin/auth_permission/edit', '修改菜单', 1, '', 11, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550243721, NULL, NULL, 14, '/admin/auth_permission/delete', '修改菜单', 1, '', 11, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550390966, 1550392488, NULL, 15, '/admin/auth_group/auth', '权限授权', 1, '', 6, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550392791, 1550395954, NULL, 16, '/admin/conf/index', '站点配置', 1, '', 10, 3);
INSERT INTO `club_auth_permission` VALUES (1, 1550392845, NULL, 1550395935, 17, '/admin/config/edit', '修改站点配置', 1, '', 16, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550392973, 1639372098, NULL, 18, '', '扩展管理', 1, 'paperclip', 0, 9);
INSERT INTO `club_auth_permission` VALUES (0, 1550393240, 1639372065, NULL, 19, '', '内容管理', 1, 'file-text', 0, 12);
INSERT INTO `club_auth_permission` VALUES (0, 1550468986, 1638155211, NULL, 20, '/admin/section/index', '单元管理', 1, '', 19, 5);
INSERT INTO `club_auth_permission` VALUES (0, 1550469033, 1638155215, NULL, 21, '/admin/category/index', '分类管理', 1, '', 19, 4);
INSERT INTO `club_auth_permission` VALUES (0, 1550469078, 1639399040, NULL, 22, '/admin/article/index', '文章管理', 1, '', 19, 3);
INSERT INTO `club_auth_permission` VALUES (0, 1550469141, NULL, NULL, 23, '/admin/section/add', '添加单元', 1, '', 20, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550469159, NULL, NULL, 24, '/admin/section/edit', '修改单元', 1, '', 20, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550469179, NULL, NULL, 25, '/admin/section/delete', '删除单元', 1, '', 20, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550469204, NULL, NULL, 26, '/admin/category/add', '添加分类', 1, '', 21, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550469225, NULL, NULL, 27, '/admin/category/edit', '修改分类', 1, '', 21, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550469248, NULL, NULL, 28, '/admin/category/delete', '删除分类', 1, '', 21, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550473786, NULL, NULL, 29, '/admin/article/add', '添加文章', 1, '', 22, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550473804, NULL, NULL, 30, '/admin/article/edit', '修改文章', 1, '', 22, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1550473823, NULL, NULL, 31, '/admin/article/delete', '删除文章', 1, '', 22, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1599104180, 1599104447, NULL, 45, ' ', '用户管理', 1, 'users', 0, 16);
INSERT INTO `club_auth_permission` VALUES (0, 1599104467, NULL, NULL, 46, '/admin/member/index', '用户管理', 1, NULL, 45, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1599104482, 1599104525, NULL, 47, '/admin/member/add', '添加用户', 1, 'None', 46, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1599104495, NULL, NULL, 48, '/admin/member/edit', '修改用户', 1, NULL, 46, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1599104513, 1639298035, NULL, 49, '/admin/member/delete', '删除用户', 1, NULL, 46, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639376473, NULL, NULL, 50, '/admin/param/index', '参数列表', 1, NULL, 18, 5);
INSERT INTO `club_auth_permission` VALUES (0, 1639376510, NULL, NULL, 51, '/admin/param/add', '添加参数', 1, NULL, 50, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639376527, NULL, NULL, 52, '/admin/param/edit', '编辑参数', 1, NULL, 50, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639376542, NULL, NULL, 53, '/admin/param/delete', '删除参数', 1, NULL, 50, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639376918, NULL, NULL, 54, '/admin/ad/index', '广告管理', 1, NULL, 18, 3);
INSERT INTO `club_auth_permission` VALUES (0, 1639376934, NULL, NULL, 55, '/admin/ad/add', '添加广告', 1, NULL, 54, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639376950, NULL, NULL, 56, '/admin/ad/delete', '删除广告', 1, NULL, 54, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639376968, NULL, NULL, 57, '/admin/ad/edit', '编辑广告', 1, NULL, 54, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639399061, NULL, NULL, 58, '/admin/page/index', '单页管理', 1, NULL, 19, 2);
INSERT INTO `club_auth_permission` VALUES (0, 1639399130, NULL, NULL, 59, '/admin/page/add', '添加单页', 1, NULL, 58, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639399147, NULL, NULL, 60, '/admin/page/edit', '编辑单页', 1, NULL, 58, 0);
INSERT INTO `club_auth_permission` VALUES (0, 1639399166, NULL, NULL, 61, '/admin/page/delete', '删除单页', 1, NULL, 58, 0);

-- ----------------------------
-- Table structure for club_auth_user
-- ----------------------------
DROP TABLE IF EXISTS `club_auth_user`;
CREATE TABLE `club_auth_user`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '管理员ID',
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '管理员账号',
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `group_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  INDEX `group_id`(`group_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of club_auth_user
-- ----------------------------
INSERT INTO `club_auth_user` VALUES (0, 1550217545, 1639373192, NULL, 1, 'admin', 'pbkdf2:sha256:150000$vI60tpUO$02a16ca54d2aa4c0296f00be65a2d3abcfbca48aebebdc41d9f66cc635149a13', 1, 1);

-- ----------------------------
-- Table structure for club_category
-- ----------------------------
DROP TABLE IF EXISTS `club_category`;
CREATE TABLE `club_category`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '分类标题',
  `alias` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '分类别名',
  `intro` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `section_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `section_id`(`section_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for club_config
-- ----------------------------
DROP TABLE IF EXISTS `club_config`;
CREATE TABLE `club_config`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '配置表ID',
  `sitename` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '站点名称',
  `metakeys` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '站点关键词',
  `metadesc` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '站点描述',
  `company` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '公司名称',
  `siteurl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '站点网址',
  `icp` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备案信息',
  `tel` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '联系电话',
  `address` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '公司地址',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of club_config
-- ----------------------------
INSERT INTO `club_config` VALUES (0, NULL, 1638172395, NULL, 1, 'FCMS123', 'FCMS32', 'FCMS123', NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for club_member
-- ----------------------------
DROP TABLE IF EXISTS `club_member`;
CREATE TABLE `club_member`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `nickname` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '昵称',
  `mobile` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户手机号',
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户邮箱',
  `openid` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '微信openid',
  `app_key` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'app_key',
  `app_secret` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'app_secret',
  `auth` smallint(6) NULL DEFAULT NULL COMMENT '1普通用户，2管理员用户',
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `type` int(11) NULL DEFAULT NULL COMMENT '类型1手机号 2邮箱 3微信',
  `integral` int(11) NULL DEFAULT NULL COMMENT '积分',
  `faceimg` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '头像',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `company` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '所属企业',
  `profession` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '所属单位',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of club_member
-- ----------------------------
INSERT INTO `club_member` VALUES (0, 1639473273, 1640223543, NULL, 1, '颠三倒四12132', '13681719001', NULL, NULL, 'b39d718f8787d7bff814664c29cd1f57', '7ae14bd2f51daef0f5f415c6716b2a78fafc88d8bfb27f001a9fd4d634d93ae3', 1, 'pbkdf2:sha256:150000$DJOpDapP$996afc2bc88037a23a342fc3ffca2b4f92851d0855116f641becc967c4bc0ce2', 1, 0, NULL, 1, NULL, NULL);

-- ----------------------------
-- Table structure for club_page
-- ----------------------------
DROP TABLE IF EXISTS `club_page`;
CREATE TABLE `club_page`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '单页ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '标题',
  `img_url` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '封面图片URL',
  `link_label` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '标识',
  `intro` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '回复内容',
  `readnum` int(11) NULL DEFAULT NULL COMMENT '阅读量',
  `praise` int(11) NULL DEFAULT NULL COMMENT '点赞量',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for club_param
-- ----------------------------
DROP TABLE IF EXISTS `club_param`;
CREATE TABLE `club_param`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `title` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数名称',
  `type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数类型',
  `type_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '参数类型名称',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for club_section
-- ----------------------------
DROP TABLE IF EXISTS `club_section`;
CREATE TABLE `club_section`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '单元ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '单元标题',
  `alias` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '单元别名',
  `intro` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;



SET FOREIGN_KEY_CHECKS = 1;
