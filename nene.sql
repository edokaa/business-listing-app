BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "businessDirectory_campus" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "businessDirectory_customer" (
	"id"	integer NOT NULL,
	"username"	varchar(50) NOT NULL,
	"password"	varchar(50) NOT NULL,
	"firstName"	varchar(50) NOT NULL,
	"lastName"	varchar(50) NOT NULL,
	"phone"	varchar(50) NOT NULL,
	"address"	varchar(255) NOT NULL,
	"avatarId_id"	integer,
	FOREIGN KEY("avatarId_id") REFERENCES "businessDirectory_avatar"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "businessDirectory_vendor" (
	"id"	integer NOT NULL,
	"username"	varchar(50) NOT NULL,
	"password"	varchar(50) NOT NULL,
	"firstName"	varchar(50) NOT NULL,
	"lastName"	varchar(50) NOT NULL,
	"phone"	varchar(50) NOT NULL,
	"address"	varchar(255) NOT NULL,
	"avatarId_id"	integer,
	FOREIGN KEY("avatarId_id") REFERENCES "businessDirectory_avatar"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "businessDirectory_admin" (
	"id"	integer NOT NULL,
	"username"	varchar(50) NOT NULL,
	"password"	varchar(50) NOT NULL,
	"lastLogin"	datetime NOT NULL,
	"avatarId_id"	integer,
	FOREIGN KEY("avatarId_id") REFERENCES "businessDirectory_avatar"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "businessDirectory_category" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"img"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "businessDirectory_review" (
	"id"	integer NOT NULL,
	"business_id"	integer NOT NULL,
	"customer_id"	integer NOT NULL,
	"createdAt"	datetime NOT NULL,
	"msg"	text NOT NULL,
	"star"	integer NOT NULL,
	FOREIGN KEY("business_id") REFERENCES "businessDirectory_business"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("customer_id") REFERENCES "businessDirectory_customer"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "businessDirectory_business" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"address"	varchar(50) NOT NULL,
	"category_id"	integer NOT NULL,
	"location_id"	integer NOT NULL,
	"owner_id"	integer NOT NULL,
	"latitude"	varchar(50) NOT NULL,
	"longitute"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"email"	varchar(50) NOT NULL,
	"landmark"	varchar(50) NOT NULL,
	"logo"	varchar(100) NOT NULL,
	"website"	varchar(50) NOT NULL,
	"addedon"	datetime NOT NULL,
	"phone"	varchar(20) NOT NULL,
	FOREIGN KEY("category_id") REFERENCES "businessDirectory_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("owner_id") REFERENCES "businessDirectory_vendor"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("location_id") REFERENCES "businessDirectory_campus"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "businessDirectory_uploads" (
	"id"	integer NOT NULL,
	"image_url"	varchar(100) NOT NULL,
	"business_id"	integer NOT NULL,
	FOREIGN KEY("business_id") REFERENCES "businessDirectory_business"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "businessDirectory_campus" VALUES (1,'UNN'),
 (2,'UNEC');
INSERT INTO "businessDirectory_customer" VALUES (1,'paul001','12345','paul','enue','0808080080','12 Baale Lamidi Musa Street, Ajah',1),
 (2,'admiral','12345','Gerald','Ekejuiba','09012345678','Odim, UNN',1);
INSERT INTO "businessDirectory_vendor" VALUES (1,'peter4ease','12345','Peter','Edoka','08081721540','12 Baale Lamidi Musa Street, Ajah',1),
 (2,'miraboy13','12345','Miracle','Adolphus','0808088080','Odim, UNN',1),
 (3,'henryben','12345','Henry','Ben','09098765432','Odim, UNN',1),
 (4,'usman123','12345','Usman','Damfodio','07012345678','Hill Top, UNN',1),
 (5,'ifeanyi001','12345','Ifeanyi','Ade','08141234567','Ikorodu, Lagos',1);
INSERT INTO "businessDirectory_category" VALUES (1,'Graphic Designs','static/uploads/thumbs/graphics_1.jpg'),
 (2,'Computer Services','static/uploads/thumbs/computer_1.jpg'),
 (3,'Mashia Spot','static/uploads/thumbs/maishai_1.jpg'),
 (4,'Cakes & Pastries','static/uploads/thumbs/cake_1.jpg'),
 (5,'Clubs','static/uploads/thumbs/night_club11_umQsEnw.jpg'),
 (6,'Games and Sports','static/uploads/thumbs/games_1.jpg'),
 (7,'Tutorial Masters','static/uploads/thumbs/clas_1.jpg'),
 (8,'Fast Food','static/uploads/thumbs/restaurant2_5hiireL.jpg'),
 (10,'Libraries','static/uploads/thumbs/library_sCI4R51.jpg'),
 (11,'POS Outlets','static/uploads/thumbs/images_17.jpeg'),
 (12,'Beauty & Salons','static/uploads/thumbs/beauty_1.jpg');
INSERT INTO "businessDirectory_review" VALUES (1,1,1,'2022-02-22 12:09:39.299071','Their Graphics is very nice.
Patronize them!!!',3);
INSERT INTO "businessDirectory_business" VALUES (1,'dPeter Graphics','12 Baale Lamidi Musa Street, Ajah',1,1,1,'1','1','','business@email.com','Container, UNN','static/uploads/logos/no-image.png','','2022-02-16 10:56:36.731160','08012345678'),
 (2,'Edoxs Services Limited','4, Grace Lodge, Odim Street, Obukpa, Nsukka',2,1,2,'3.123213214214','0.123123231232','','business@email.com','Container, UNN','static/uploads/logos/no-image.png','','2022-02-17 10:56:36.731160','08012345678'),
 (3,'Derah Cakes','Odim, UNN',4,1,2,'0.21421414124214','0.1321242142142','Delicious Cakes and pastries. Place an order now and you won''t regret it.','info@derah_cakes.services','Container, UNN','static/uploads/logos/derah_cakes.png','https://derahcakes.services','2022-02-22 10:56:36.731160','08012345678'),
 (4,'Volts Night Life','Asabana Hotel, Nsukka',5,1,1,'0.912421424','0.2121412412','Volts is a place to be.','voltsnightlife@gmail.com','Container, UNN','static/uploads/logos/volts.jpg','https://volts.com','2022-02-22 11:32:09.587068','08012345678'),
 (5,'Henry Ben Academy','New Engineering Annex',7,1,3,'0.124431412','0.24242424','Smash all your courses ''A'' with henry ben','henryben@edu.ng','New Engineering Annex','static/uploads/logos/no-image_EEeuzOC.png','https://henryben.edu.ng','2022-02-22 12:18:04.922250','09012564789'),
 (6,'Usman Maishai','SUB, Unn',3,1,4,'-2.12242143414','-1.124214214','W prepare the best Maishai in the whole of UNN','usmn_maishai@gmail.com','SUB, Unn','static/uploads/logos/no-image_XS7CIb3.png','','2022-02-22 12:46:18.958401','08045617891'),
 (7,'Coscharis Business Centre','Law Annex, Unec',2,2,5,'0.323232434324','0,1323213213','Photocopy nd buy course materials at  very cheap rate','coscharis@biz.com','Faculty of Law, UNEC','static/uploads/logos/Untitled-1.png','coscharis.biz.oom','2022-02-24 20:32:07.907084','+234 808 172 1540');
INSERT INTO "businessDirectory_uploads" VALUES (1,'static/uploads/images/cake_1.jpg',3),
 (2,'static/uploads/images/derah_cakes.png',3),
 (3,'static/uploads/images/catering.png',3),
 (4,'static/uploads/images/discount.png',3),
 (5,'static/uploads/images/party_copy.png',4),
 (6,'static/uploads/images/business_hero.png',1),
 (7,'static/uploads/images/monica_copy.png',4),
 (8,'static/uploads/images/computer_1.jpg',2),
 (9,'static/uploads/images/graphics_1.jpg',2),
 (10,'static/uploads/images/container_1.jpg',1),
 (11,'static/uploads/images/graphics_1_MZW18vS.jpg',1),
 (12,'static/uploads/images/clas_1.jpg',5),
 (13,'static/uploads/images/night_club1_XnhBedZ.jpg',4),
 (14,'static/uploads/images/night_club11_cOOxM6M.jpg',4),
 (15,'static/uploads/images/oro-nightclub_85A6MdA.jpg',4),
 (16,'static/uploads/images/mai-sahyi.png',6),
 (17,'static/uploads/images/maishai_2.jpg',6),
 (18,'static/uploads/images/maishai_1.jpg',6),
 (19,'static/uploads/images/discount_cnInL8G.png',6);
CREATE INDEX IF NOT EXISTS "businessDirectory_customer_avatarId_id_3d126c40" ON "businessDirectory_customer" (
	"avatarId_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_vendor_avatarId_id_9c8dcc97" ON "businessDirectory_vendor" (
	"avatarId_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_admin_avatarId_id_e00ac5e8" ON "businessDirectory_admin" (
	"avatarId_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_review_business_id_1a45c7f7" ON "businessDirectory_review" (
	"business_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_review_customer_id_4595810d" ON "businessDirectory_review" (
	"customer_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_business_category_id_028f1358" ON "businessDirectory_business" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_business_location_id_566308ab" ON "businessDirectory_business" (
	"location_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_business_owner_id_7a8768ae" ON "businessDirectory_business" (
	"owner_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_uploads_business_id_1e5d4db7" ON "businessDirectory_uploads" (
	"business_id"
);
COMMIT;
