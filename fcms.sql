/*
Navicat MySQL Data Transfer

Source Server         : sars
Source Server Version : 50616
Source Host           : rm-2ze1kb71f9c1nodego.mysql.rds.aliyuncs.com:3306
Source Database       : sars

Target Server Type    : MYSQL
Target Server Version : 50616
File Encoding         : 65001

Date: 2020-02-17 12:51:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cms_article
-- ----------------------------
DROP TABLE IF EXISTS `cms_article`;
CREATE TABLE `cms_article` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `title` varchar(50) NOT NULL COMMENT '文章标题',
  `alias` varchar(50) DEFAULT NULL COMMENT '文章别名',
  `metakeys` varchar(100) DEFAULT NULL COMMENT 'SEO关键词',
  `metadesc` varchar(300) DEFAULT NULL COMMENT 'SEO描述',
  `intro` varchar(300) DEFAULT NULL COMMENT '简介',
  `img` varchar(200) DEFAULT NULL COMMENT '文章图片',
  `content` text COMMENT '正文',
  `istop` tinyint(1) DEFAULT NULL COMMENT '是否置顶',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  `author` varchar(50) DEFAULT NULL COMMENT '来源/作者',
  `hits` int(11) DEFAULT NULL COMMENT '点击量',
  `praise` int(11) DEFAULT NULL COMMENT '点赞量',
  `start_time` int(11) DEFAULT NULL COMMENT '开始时间',
  `end_time` int(11) DEFAULT NULL COMMENT '截止时间',
  `category_id` int(11) DEFAULT NULL,
  `section_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `section_id` (`section_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of cms_article
-- ----------------------------
INSERT INTO `cms_article` VALUES ('1', '1550550129', '1550551058', '1550551063', '1', '大叔大婶多是', 'ew', 'we', null, null, 'upload\\vVAXfuLBGS2MzCcb8sZ3I1D5q7yOPoxd.jpg', '<p>dsdsds<img src=\"http://127.0.0.1:5000/static/upload/image/2019219/122008524441.jpg\" title=\"569c5d2793d1b.jpg\" alt=\"569c5d2793d1b.jpg\"/></p>', '1', '0', '2', 'we', null, null, '2019', null, '2', '2');
INSERT INTO `cms_article` VALUES ('0', '1550550154', '1550558217', null, '2', '大叔大婶多是', 'ew', 'we', 'we', null, 'upload\\vVAXfuLBGS2MzCcb8sZ3I1D5q7yOPoxd.jpg', '<p>&lt;p&gt;dsdsds&lt;img src=&quot;http://127.0.0.1:5000/static/upload/image/2019219/122008524441.jpg&quot; title=&quot;569c5d2793d1b.jpg&quot; alt=&quot;569c5d2793d1b.jpg&quot;/&gt;&lt;/p&gt;</p>', '1', '1', '2', 'we', null, null, '1872000', null, '2', '2');
INSERT INTO `cms_article` VALUES ('0', '1550550931', '1550558107', null, '3', '未2aqwqwewwe', '32', 'd\'swqqw', 'd\'swqqw', null, 'upload\\3pjVS9OCYLvIEa1NMstUdHyilew42chR.jpg', '<p>&lt;p&gt;&amp;lt;p&amp;gt;&amp;amp;lt;p&amp;amp;gt;&amp;amp;amp;lt;p&amp;amp;amp;gt;时代大厦&amp;amp;amp;lt;/p&amp;amp;amp;gt;&amp;amp;lt;/p&amp;amp;gt;&amp;lt;/p&amp;gt;ewewewwe&lt;/p&gt;</p>', '0', '1', '0', '3232', null, null, '1550851200', null, '1', '2');
INSERT INTO `cms_article` VALUES ('0', '1550721762', null, null, '4', '212121', '21', '23', null, null, null, '<p>weew</p>', '0', '1', '0', '', null, null, '1549641600', null, '2', '2');
INSERT INTO `cms_article` VALUES ('1', '1550721972', null, '1550739664', '5', '434334', '4334', '34433', null, null, null, '<p>3443</p>', '0', '1', '0', '', null, null, '1549641600', null, '2', '2');
INSERT INTO `cms_article` VALUES ('0', '1550739651', null, null, '6', '嗯我若翁无', '', '', null, null, null, '<p>神鼎飞丹砂</p>', '0', '1', '0', '', null, null, '1550851200', null, '2', '2');

-- ----------------------------
-- Table structure for cms_auth_group
-- ----------------------------
DROP TABLE IF EXISTS `cms_auth_group`;
CREATE TABLE `cms_auth_group` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限组ID',
  `title` varchar(100) DEFAULT NULL COMMENT '权限组名称',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否发布',
  `permissions` text COMMENT '规则列表',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of cms_auth_group
-- ----------------------------
INSERT INTO `cms_auth_group` VALUES ('0', '1550215694', '1552031793', null, '1', '系统管理员', '1', '1,2,3,4,5,6,7,8,9,15,10,11,12,13,14,16,18,19,20,23,24,25,21,26,27,28,22,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44');
INSERT INTO `cms_auth_group` VALUES ('0', '1550215702', '1550216482', null, '2', '普通管理员', '1', '1,2');

-- ----------------------------
-- Table structure for cms_auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `cms_auth_permission`;
CREATE TABLE `cms_auth_permission` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限规则ID',
  `per_name` varchar(50) DEFAULT NULL COMMENT '规则名称（控制器）',
  `per_title` varchar(50) DEFAULT NULL COMMENT '菜单名称',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否发布',
  `icon` varchar(30) DEFAULT NULL COMMENT '图标',
  `pid` int(11) DEFAULT NULL COMMENT '父级ID',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of cms_auth_permission
-- ----------------------------
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240302', '1550334863', null, '1', '', '管理员管理', '1', 'Hui-iconfont-user-zhanzhang', '0', '7');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240334', null, null, '2', '/admin/auth_user/index', '管理员管理', '1', '', '1', '5');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240396', null, null, '3', '/admin/auth_user/add', '添加管理员', '1', '', '2', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240466', null, null, '4', '/admin/auth_user/edit', '修改管理员', '1', '', '2', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240489', null, null, '5', '/admin/auth_user/delete', '删除管理员', '1', '', '2', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240552', null, null, '6', '/admin/auth_group/index', '权限组管理', '1', '', '1', '3');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240612', null, null, '7', '/admin/auth_group/add', '添加权限组', '1', '', '6', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240670', null, null, '8', '/admin/auth_group/edit', '修改权限组', '1', '', '6', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240708', null, null, '9', '/admin/auth_group/delete', '删除权限组', '1', '', '6', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240884', '1550393171', null, '10', '', '站点管理', '1', 'Hui-iconfont-system', '0', '5');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550240926', null, null, '11', '/admin/auth_permission/index', '菜单(权限)管理', '1', '', '10', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550243521', null, null, '12', '/admin/auth_permission/add', '添加菜单', '1', '', '11', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550243703', null, null, '13', '/admin/auth_permission/edit', '修改菜单', '1', '', '11', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550243721', null, null, '14', '/admin/auth_permission/delete', '修改菜单', '1', '', '11', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550390966', '1550392488', null, '15', '/admin/auth_group/auth', '权限授权', '1', '', '6', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550392791', '1550395954', null, '16', '/admin/conf/index', '站点配置', '1', '', '10', '3');
INSERT INTO `cms_auth_permission` VALUES ('1', '1550392845', null, '1550395935', '17', '/admin/config/edit', '修改站点配置', '1', '', '16', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550392973', '1550393621', null, '18', '', '扩展管理', '1', 'Hui-iconfont-fenlei', '0', '9');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550393240', '1550393252', null, '19', '', '内容管理', '1', 'Hui-iconfont-news', '0', '12');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550468986', '1551345045', null, '20', '/admin/section/index', '单元管理', '0', '', '19', '5');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469033', '1551345048', null, '21', '/admin/category/index', '分类管理', '0', '', '19', '4');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469078', '1551345052', null, '22', '/admin/article/index', '文章管理', '0', '', '19', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469141', null, null, '23', '/admin/section/add', '添加单元', '1', '', '20', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469159', null, null, '24', '/admin/section/edit', '修改单元', '1', '', '20', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469179', null, null, '25', '/admin/section/delete', '删除单元', '1', '', '20', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469204', null, null, '26', '/admin/category/add', '添加分类', '1', '', '21', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469225', null, null, '27', '/admin/category/edit', '修改分类', '1', '', '21', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550469248', null, null, '28', '/admin/category/delete', '删除分类', '1', '', '21', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550473786', null, null, '29', '/admin/article/add', '添加文章', '1', '', '22', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550473804', null, null, '30', '/admin/article/edit', '修改文章', '1', '', '22', '0');
INSERT INTO `cms_auth_permission` VALUES ('0', '1550473823', null, null, '31', '/admin/article/delete', '删除文章', '1', '', '22', '0');

-- ----------------------------
-- Table structure for cms_auth_user
-- ----------------------------
DROP TABLE IF EXISTS `cms_auth_user`;
CREATE TABLE `cms_auth_user` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '管理员ID',
  `username` varchar(50) DEFAULT NULL COMMENT '管理员账号',
  `password` varchar(128) NOT NULL COMMENT '密码',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否发布',
  `group_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `group_id` (`group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of cms_auth_user
-- ----------------------------
INSERT INTO `cms_auth_user` VALUES ('0', '1550217545', null, null, '2', 'admin', 'pbkdf2:sha256:150000$vI60tpUO$02a16ca54d2aa4c0296f00be65a2d3abcfbca48aebebdc41d9f66cc635149a13', '1', '1');

-- ----------------------------
-- Table structure for cms_category
-- ----------------------------
DROP TABLE IF EXISTS `cms_category`;
CREATE TABLE `cms_category` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `title` varchar(50) NOT NULL COMMENT '分类标题',
  `alias` varchar(50) DEFAULT NULL COMMENT '分类别名',
  `intro` varchar(300) DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  `section_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `section_id` (`section_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for cms_config
-- ----------------------------
DROP TABLE IF EXISTS `cms_config`;
CREATE TABLE `cms_config` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '配置表ID',
  `sitename` varchar(50) DEFAULT NULL COMMENT '站点名称',
  `metakeys` varchar(100) DEFAULT NULL COMMENT '站点关键词',
  `metadesc` varchar(300) DEFAULT NULL COMMENT '站点描述',
  `company` varchar(100) DEFAULT NULL COMMENT '公司名称',
  `siteurl` varchar(255) DEFAULT NULL COMMENT '站点网址',
  `icp` varchar(100) DEFAULT NULL COMMENT '备案信息',
  `tel` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `address` varchar(300) DEFAULT NULL COMMENT '公司地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for cms_page
-- ----------------------------
DROP TABLE IF EXISTS `cms_page`;
CREATE TABLE `cms_page` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '单页ID',
  `title` varchar(50) NOT NULL COMMENT '标题',
  `img_url` varchar(300) DEFAULT NULL COMMENT '封面图片URL',
  `link_label` varchar(60) DEFAULT NULL COMMENT '标识',
  `intro` varchar(300) DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  `content` text COMMENT '回复内容',
  `readnum` int(11) DEFAULT NULL COMMENT '阅读量',
  `praise` int(11) DEFAULT NULL COMMENT '点赞量',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of cms_page
-- ----------------------------

-- ----------------------------
-- Table structure for cms_section
-- ----------------------------
DROP TABLE IF EXISTS `cms_section`;
CREATE TABLE `cms_section` (
  `is_delete` tinyint(1) DEFAULT NULL COMMENT '是否删除 True为删除',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '修改时间',
  `delete_time` int(11) DEFAULT NULL COMMENT '删除时间',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '单元ID',
  `title` varchar(50) NOT NULL COMMENT '单元标题',
  `alias` varchar(50) DEFAULT NULL COMMENT '单元别名',
  `intro` varchar(300) DEFAULT NULL COMMENT '描述',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否发布',
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

