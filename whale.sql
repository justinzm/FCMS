/*
 Navicat Premium Data Transfer

 Source Server         : 极橙 47.92.208.84
 Source Server Type    : MySQL
 Source Server Version : 50649
 Source Host           : localhost:3306
 Source Schema         : whale

 Target Server Type    : MySQL
 Target Server Version : 50649
 File Encoding         : 65001

 Date: 24/06/2021 10:49:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for w_article
-- ----------------------------
DROP TABLE IF EXISTS `w_article`;
CREATE TABLE `w_article`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_article
-- ----------------------------
INSERT INTO `w_article` VALUES (1, 1550550129, 1550551058, 1550551063, 1, '大叔大婶多是', 'ew', 'we', NULL, NULL, 'upload\\vVAXfuLBGS2MzCcb8sZ3I1D5q7yOPoxd.jpg', '<p>dsdsds<img src=\"http://127.0.0.1:5000/static/upload/image/2019219/122008524441.jpg\" title=\"569c5d2793d1b.jpg\" alt=\"569c5d2793d1b.jpg\"/></p>', 1, 0, 2, 'we', NULL, NULL, 2019, NULL, 2, 2);
INSERT INTO `w_article` VALUES (1, 1550550154, 1550558217, 1624438792, 2, '大叔大婶多是', 'ew', 'we', 'we', NULL, 'upload\\vVAXfuLBGS2MzCcb8sZ3I1D5q7yOPoxd.jpg', '<p>&lt;p&gt;dsdsds&lt;img src=&quot;http://127.0.0.1:5000/static/upload/image/2019219/122008524441.jpg&quot; title=&quot;569c5d2793d1b.jpg&quot; alt=&quot;569c5d2793d1b.jpg&quot;/&gt;&lt;/p&gt;</p>', 1, 1, 2, 'we', NULL, NULL, 1872000, NULL, 2, 2);
INSERT INTO `w_article` VALUES (1, 1550550931, 1550558107, 1624438792, 3, '未2aqwqwewwe', '32', 'd\'swqqw', 'd\'swqqw', NULL, 'upload\\3pjVS9OCYLvIEa1NMstUdHyilew42chR.jpg', '<p>&lt;p&gt;&amp;lt;p&amp;gt;&amp;amp;lt;p&amp;amp;gt;&amp;amp;amp;lt;p&amp;amp;amp;gt;时代大厦&amp;amp;amp;lt;/p&amp;amp;amp;gt;&amp;amp;lt;/p&amp;amp;gt;&amp;lt;/p&amp;gt;ewewewwe&lt;/p&gt;</p>', 0, 1, 0, '3232', NULL, NULL, 1550851200, NULL, 1, 2);
INSERT INTO `w_article` VALUES (1, 1550721762, NULL, 1624438792, 4, '212121', '21', '23', NULL, NULL, NULL, '<p>weew</p>', 0, 1, 0, '', NULL, NULL, 1549641600, NULL, 2, 2);
INSERT INTO `w_article` VALUES (1, 1550721972, NULL, 1550739664, 5, '434334', '4334', '34433', NULL, NULL, NULL, '<p>3443</p>', 0, 1, 0, '', NULL, NULL, 1549641600, NULL, 2, 2);
INSERT INTO `w_article` VALUES (1, 1550739651, NULL, 1624438792, 6, '嗯我若翁无', '', '', NULL, NULL, NULL, '<p>神鼎飞丹砂</p>', 0, 1, 0, '', NULL, NULL, 1550851200, NULL, 2, 2);

-- ----------------------------
-- Table structure for w_auth_group
-- ----------------------------
DROP TABLE IF EXISTS `w_auth_group`;
CREATE TABLE `w_auth_group`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限组ID',
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '权限组名称',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `permissions` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '规则列表',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_auth_group
-- ----------------------------
INSERT INTO `w_auth_group` VALUES (0, 1550215694, 1624502413, NULL, 1, '系统管理员', 1, '1,2,3,4,5,6,7,8,9,15,10,11,12,13,14,16,18,46,47,48,49,19,20,23,24,25,21,26,27,28,22,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45');
INSERT INTO `w_auth_group` VALUES (0, 1550215702, 1550216482, NULL, 2, '普通管理员', 1, '1,2');

-- ----------------------------
-- Table structure for w_auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `w_auth_permission`;
CREATE TABLE `w_auth_permission`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 50 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_auth_permission
-- ----------------------------
INSERT INTO `w_auth_permission` VALUES (0, 1550240302, 1550334863, NULL, 1, '', '管理员管理', 1, 'Hui-iconfont-user-zhanzhang', 0, 7);
INSERT INTO `w_auth_permission` VALUES (0, 1550240334, NULL, NULL, 2, '/admin/auth_user/index', '管理员管理', 1, '', 1, 5);
INSERT INTO `w_auth_permission` VALUES (0, 1550240396, NULL, NULL, 3, '/admin/auth_user/add', '添加管理员', 1, '', 2, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550240466, NULL, NULL, 4, '/admin/auth_user/edit', '修改管理员', 1, '', 2, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550240489, NULL, NULL, 5, '/admin/auth_user/delete', '删除管理员', 1, '', 2, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550240552, NULL, NULL, 6, '/admin/auth_group/index', '权限组管理', 1, '', 1, 3);
INSERT INTO `w_auth_permission` VALUES (0, 1550240612, NULL, NULL, 7, '/admin/auth_group/add', '添加权限组', 1, '', 6, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550240670, NULL, NULL, 8, '/admin/auth_group/edit', '修改权限组', 1, '', 6, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550240708, NULL, NULL, 9, '/admin/auth_group/delete', '删除权限组', 1, '', 6, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550240884, 1550393171, NULL, 10, '', '站点管理', 1, 'Hui-iconfont-system', 0, 5);
INSERT INTO `w_auth_permission` VALUES (0, 1550240926, NULL, NULL, 11, '/admin/auth_permission/index', '菜单(权限)管理', 1, '', 10, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550243521, NULL, NULL, 12, '/admin/auth_permission/add', '添加菜单', 1, '', 11, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550243703, NULL, NULL, 13, '/admin/auth_permission/edit', '修改菜单', 1, '', 11, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550243721, NULL, NULL, 14, '/admin/auth_permission/delete', '修改菜单', 1, '', 11, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550390966, 1550392488, NULL, 15, '/admin/auth_group/auth', '权限授权', 1, '', 6, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550392791, 1550395954, NULL, 16, '/admin/conf/index', '站点配置', 1, '', 10, 3);
INSERT INTO `w_auth_permission` VALUES (1, 1550392845, NULL, 1550395935, 17, '/admin/config/edit', '修改站点配置', 1, '', 16, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550392973, 1550393621, NULL, 18, '', '扩展管理', 1, 'Hui-iconfont-fenlei', 0, 9);
INSERT INTO `w_auth_permission` VALUES (0, 1550393240, 1550393252, NULL, 19, '', '内容管理', 1, 'Hui-iconfont-news', 0, 12);
INSERT INTO `w_auth_permission` VALUES (0, 1550468986, 1624177475, NULL, 20, '/admin/section/index', '单元管理', 1, '', 19, 5);
INSERT INTO `w_auth_permission` VALUES (0, 1550469033, 1624177438, NULL, 21, '/admin/category/index', '分类管理', 1, '', 19, 4);
INSERT INTO `w_auth_permission` VALUES (0, 1550469078, 1624177453, NULL, 22, '/admin/article/index', '文章管理', 1, '', 19, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550469141, NULL, NULL, 23, '/admin/section/add', '添加单元', 1, '', 20, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550469159, NULL, NULL, 24, '/admin/section/edit', '修改单元', 1, '', 20, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550469179, NULL, NULL, 25, '/admin/section/delete', '删除单元', 1, '', 20, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550469204, NULL, NULL, 26, '/admin/category/add', '添加分类', 1, '', 21, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550469225, NULL, NULL, 27, '/admin/category/edit', '修改分类', 1, '', 21, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550469248, NULL, NULL, 28, '/admin/category/delete', '删除分类', 1, '', 21, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550473786, NULL, NULL, 29, '/admin/article/add', '添加文章', 1, '', 22, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550473804, NULL, NULL, 30, '/admin/article/edit', '修改文章', 1, '', 22, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1550473823, NULL, NULL, 31, '/admin/article/delete', '删除文章', 1, '', 22, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624426591, 1624427207, NULL, 32, ' ', '微信公号管理', 1, 'Hui-iconfont-share-weixin', 0, 8);
INSERT INTO `w_auth_permission` VALUES (0, 1624427341, 1624427374, NULL, 33, '/admin/wx_reply/index', '关注回复管理', 1, 'None', 32, 6);
INSERT INTO `w_auth_permission` VALUES (0, 1624427417, NULL, NULL, 34, '/admin/wx_text/index', '文本回复管理', 1, NULL, 32, 5);
INSERT INTO `w_auth_permission` VALUES (0, 1624427456, NULL, NULL, 35, '/admin/wx_text/add', '添加文本回复', 1, NULL, 34, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427472, NULL, NULL, 36, '/admin/wx_text/edit', '编辑文本回复', 1, NULL, 34, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427489, NULL, NULL, 37, '/admin/wx_text/delete', '删除文本回复', 1, NULL, 34, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427626, NULL, NULL, 38, '/admin/wx_imgtext/index', '图文回复管理', 1, NULL, 32, 4);
INSERT INTO `w_auth_permission` VALUES (0, 1624427646, NULL, NULL, 39, '/admin/wx_imgtext/add', '添加图文回复', 1, NULL, 38, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427667, NULL, NULL, 40, '/admin/wx_imgtext/edit', '编辑图文回复', 1, NULL, 38, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427687, NULL, NULL, 41, '/admin/wx_imgtext/delete', '删除图文回复', 1, NULL, 38, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427717, NULL, NULL, 42, '/admin/wx_diymenu/index', '微信自定义菜单', 1, NULL, 32, 3);
INSERT INTO `w_auth_permission` VALUES (0, 1624427742, NULL, NULL, 43, '/admin/wx_diymenu/add', '添加自定义菜单', 1, NULL, 42, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427764, NULL, NULL, 44, '/admin/wx_diymenu/edit', '编辑自定义菜单', 1, NULL, 42, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624427800, NULL, NULL, 45, '/admin/wx_diymenu/delete', '删除自定义菜单', 1, NULL, 42, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624501706, NULL, NULL, 46, '/admin/param/index', '参数管理', 1, NULL, 18, 5);
INSERT INTO `w_auth_permission` VALUES (0, 1624502347, NULL, NULL, 47, '/admin/param/add', '添加参数', 1, NULL, 46, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624502363, NULL, NULL, 48, '/admin/param/edit', '编辑参数', 1, NULL, 46, 0);
INSERT INTO `w_auth_permission` VALUES (0, 1624502380, NULL, NULL, 49, '/admin/param/delete', '删除参数', 1, NULL, 46, 0);

-- ----------------------------
-- Table structure for w_auth_user
-- ----------------------------
DROP TABLE IF EXISTS `w_auth_user`;
CREATE TABLE `w_auth_user`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_auth_user
-- ----------------------------
INSERT INTO `w_auth_user` VALUES (0, 1550217545, NULL, NULL, 1, 'admin', 'pbkdf2:sha256:150000$vI60tpUO$02a16ca54d2aa4c0296f00be65a2d3abcfbca48aebebdc41d9f66cc635149a13', 1, 1);

-- ----------------------------
-- Table structure for w_category
-- ----------------------------
DROP TABLE IF EXISTS `w_category`;
CREATE TABLE `w_category`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_category
-- ----------------------------

-- ----------------------------
-- Table structure for w_config
-- ----------------------------
DROP TABLE IF EXISTS `w_config`;
CREATE TABLE `w_config`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_config
-- ----------------------------
INSERT INTO `w_config` VALUES (0, NULL, NULL, NULL, 1, 'a', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for w_member
-- ----------------------------
DROP TABLE IF EXISTS `w_member`;
CREATE TABLE `w_member`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_member
-- ----------------------------

-- ----------------------------
-- Table structure for w_page
-- ----------------------------
DROP TABLE IF EXISTS `w_page`;
CREATE TABLE `w_page`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_page
-- ----------------------------

-- ----------------------------
-- Table structure for w_param
-- ----------------------------
DROP TABLE IF EXISTS `w_param`;
CREATE TABLE `w_param`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_param
-- ----------------------------

-- ----------------------------
-- Table structure for w_section
-- ----------------------------
DROP TABLE IF EXISTS `w_section`;
CREATE TABLE `w_section`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_section
-- ----------------------------

-- ----------------------------
-- Table structure for w_wx_diymenu
-- ----------------------------
DROP TABLE IF EXISTS `w_wx_diymenu`;
CREATE TABLE `w_wx_diymenu`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `pid` int(11) NULL DEFAULT NULL COMMENT '父ID',
  `keyword` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '关键词',
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '菜单标题',
  `type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '类型',
  `sort` int(11) NULL DEFAULT NULL COMMENT '排序',
  `url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '链接地址',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_wx_diymenu
-- ----------------------------
INSERT INTO `w_wx_diymenu` VALUES (0, 1624438403, NULL, NULL, 1, 0, '按钮', '按钮一', 'click', 3, NULL, 1);
INSERT INTO `w_wx_diymenu` VALUES (0, 1624438418, NULL, NULL, 2, 0, 'an2', '按钮二', 'click', 2, NULL, 1);
INSERT INTO `w_wx_diymenu` VALUES (0, 1624438452, NULL, NULL, 3, 1, 'baidu', '百度', 'click', NULL, 'http://www.baidu.com', 1);

-- ----------------------------
-- Table structure for w_wx_imgtext
-- ----------------------------
DROP TABLE IF EXISTS `w_wx_imgtext`;
CREATE TABLE `w_wx_imgtext`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `keyword` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '关键词',
  `title` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '图文标题',
  `img_url` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '封面链接',
  `url` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '链接正文',
  `is_img` tinyint(1) NULL DEFAULT NULL COMMENT '是否显示封面',
  `intro` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '图文简介',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '回复内容',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `type` int(11) NULL DEFAULT NULL COMMENT '1完全2模糊匹配',
  `readnum` int(11) NULL DEFAULT NULL COMMENT '阅读量',
  `praise` int(11) NULL DEFAULT NULL COMMENT '点赞量',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_wx_imgtext
-- ----------------------------
INSERT INTO `w_wx_imgtext` VALUES (0, 1624438680, NULL, NULL, 1, 'b', '图文标题图文标题', 'upload/X8jbisKCUklDYrHxAWEo1V5P6BRNfdGt.jpeg', NULL, 1, '图文简介图文简介图文简介图文简介图文简介', '<p><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right; background-color: rgb(255, 255, 255);\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); font-family: &quot;Microsoft Yahei&quot;, &quot;Hiragino Sans GB&quot;, &quot;Helvetica Neue&quot;, Helvetica, tahoma, arial, &quot;WenQuanYi Micro Hei&quot;, Verdana, sans-serif, 宋体; font-size: 14px; text-align: right;\">图文内容</span></p>', 1, 1, 0, 0);

-- ----------------------------
-- Table structure for w_wx_reply
-- ----------------------------
DROP TABLE IF EXISTS `w_wx_reply`;
CREATE TABLE `w_wx_reply`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '回复内容',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_wx_reply
-- ----------------------------
INSERT INTO `w_wx_reply` VALUES (0, 1550550154, 1624436532, NULL, 1, 'xxwer');

-- ----------------------------
-- Table structure for w_wx_text
-- ----------------------------
DROP TABLE IF EXISTS `w_wx_text`;
CREATE TABLE `w_wx_text`  (
  `is_delete` tinyint(1) NULL DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) NULL DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) NULL DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `keyword` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '关键词',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '回复内容',
  `status` tinyint(1) NULL DEFAULT NULL COMMENT '是否发布',
  `type` int(11) NULL DEFAULT NULL COMMENT '1完全2模糊匹配',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of w_wx_text
-- ----------------------------
INSERT INTO `w_wx_text` VALUES (0, 1624438623, NULL, NULL, 1, 'a', 'aaasss/发抖/磕头', 1, 1);

SET FOREIGN_KEY_CHECKS = 1;
