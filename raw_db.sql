BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "businessDirectory_business" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(50) NOT NULL,
	"logo"	varchar(100) NOT NULL,
	"landmark"	varchar(50) NOT NULL,
	"email"	varchar(50) NOT NULL,
	"website"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"address"	varchar(100) NOT NULL,
	"latitude"	varchar(50) NOT NULL,
	"phone"	varchar(20) NOT NULL,
	"category_id"	integer NOT NULL,
	"location_id"	integer NOT NULL,
	"owner_id"	integer NOT NULL,
	"added_on"	datetime NOT NULL,
	"longitude"	varchar(50) NOT NULL,
	FOREIGN KEY("owner_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("location_id") REFERENCES "businessDirectory_campus"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "businessDirectory_category"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_vendorbusinessrequest" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"business_name"	varchar(50) NOT NULL,
	"is_added"	bool NOT NULL,
	"campus_id"	integer NOT NULL,
	"category_id"	integer NOT NULL,
	"vendor_id"	integer NOT NULL,
	"sent_at"	datetime NOT NULL,
	FOREIGN KEY("vendor_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "businessDirectory_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("campus_id") REFERENCES "businessDirectory_campus"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_notification" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	varchar(50) NOT NULL,
	"msg"	text NOT NULL,
	"receiver_id"	integer NOT NULL,
	"sent_at"	datetime NOT NULL,
	"is_read"	bool NOT NULL,
	FOREIGN KEY("receiver_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_customermessage" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"msg"	text NOT NULL,
	"sent_at"	datetime NOT NULL,
	"receiver_id"	integer NOT NULL,
	"is_read"	bool NOT NULL,
	FOREIGN KEY("receiver_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(150) NOT NULL,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"is_admin"	bool NOT NULL,
	"is_vendor"	bool NOT NULL,
	"is_customer"	bool NOT NULL,
	"phone"	varchar(20) NOT NULL,
	"photo_url"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "businessDirectory_uploads" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"business_id"	integer NOT NULL,
	"image_url"	varchar(100) NOT NULL,
	FOREIGN KEY("business_id") REFERENCES "businessDirectory_business"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_category" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(50) NOT NULL,
	"img"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "businessDirectory_customersavedlisting" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"saved_at"	datetime NOT NULL,
	"business_id"	integer NOT NULL,
	"customer_id"	integer NOT NULL,
	FOREIGN KEY("customer_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("business_id") REFERENCES "businessDirectory_business"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_review" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"star"	integer NOT NULL,
	"msg"	text NOT NULL,
	"created_at"	datetime NOT NULL,
	"business_id"	integer NOT NULL,
	"customer_id"	integer NOT NULL,
	FOREIGN KEY("customer_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("business_id") REFERENCES "businessDirectory_business"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_campus" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "businessDirectory_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "businessDirectory_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "businessDirectory_user"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "businessDirectory_business" VALUES (1,'Miracle Keys Academy','static/uploads/logos/m4_acadrmy_2fPvYbn.jpg','Odim Gate','info@miraclekeys.com','https://www.miraclekeys.com','Did you know you can become a professional pianist in less than 3 months? YES YOU CAN! Contact us today. You have no excuse!!!!','Ejuona, Obukpa, Nsukka.','6.8644553','08127872082',7,1,2,'2022-03-07 13:31:56.816074','7.4060996');
INSERT INTO "businessDirectory_business" VALUES (5,'mmm','static/uploads/logos/no-image.png','Odim Gate','peter.edoka.242464@unn.edu.ng','https://www.miraclekeys.com','ashjkdfhkjdasf','Ejuona, Obukpa, Nsukka.','6.8644553','08026889782',1,2,2,'2022-03-07 13:31:57.038874','7.4060996');
INSERT INTO "businessDirectory_business" VALUES (6,'Ogadi Ventures','static/uploads/logos/images_17.jpeg','Coscharis Lecture Hall','info@ogadiventures.services','https://www.ogadiventures.services','We are dealers in all kinds of importation and exportation business, general machandize. POS, Withdrawal, transfer, bitcoin, etc.','12, Ozumba Drive, Unec, Enugu State','6.8644553','090154214561',11,2,12,'2022-03-08 10:12:41.408856','7.4060996');
INSERT INTO "businessDirectory_business" VALUES (7,'Ogadi UNN Ventures','static/uploads/logos/no-image.png','','','','','','6.8644553','',11,1,12,'2022-03-07 13:31:57.402055','7.4060996');
INSERT INTO "businessDirectory_business" VALUES (10,'Prosquino Ltd','static/uploads/logos/Untitled-1_BcwowJL.png','Nsukka Fire State','adol@adol.com','','This is prosquino Ltd. we are very good. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Excepturi, dolores, quibusdam architecto voluptatem amet fugiat nesciunt placeat provident cumque accusamus itaque.','Near Fire Station, Nsukka, UNN','6.8644553','080PROSQUINO',4,1,2,'2022-03-07 13:31:57.755674','7.4060996');
INSERT INTO "businessDirectory_business" VALUES (11,'Ogadi Nite Club','static/uploads/logos/gift.jpg','Asabana Hotels, Nsukka','a@b.c','https://b.c','Your no 1 night life spot. come enjoy, cruise and relax from the stress of lectures.','Asabana Hotels, Nsukka','6.8644553','0808080808',5,1,12,'2022-03-08 10:20:37.068670','7.4060996');
INSERT INTO "businessDirectory_business" VALUES (12,'Dyneco Refinery','static/uploads/logos/not_imposter.png','Abuja Building','info@dyneforefinery.com','https://dynecorefinery.com','11 Jan 2022 — I want to ask that is there any way to use google map APIs free with python to extract (addesses, distance, traffic) information.
2 answers
  ·  0 votes: No, there is no free lunch. Google''s services are payed (for normal usage), but there ...
Plot points in google map with python with google api
29 Apr 2022
google maps direction api: python vs javascript - Stack Overflow
20 Dec 2021
How to replace a Google Maps Static API URL with a Mapbox ...
22 Apr 2020
Adding Google Maps API Keys to Python program
16 Mar 2021
More results from stackoverflow.com','More results from stackoverflow.com','6.8644553','08080808080',3,1,13,'2022-10-14 15:18:08.904964','7.4060996');
INSERT INTO "businessDirectory_vendorbusinessrequest" VALUES (1,'Miracle in four Dimensions',1,1,2,2,'2022-03-02 14:28:40.231602');
INSERT INTO "businessDirectory_vendorbusinessrequest" VALUES (5,'Prosquino Ltd',1,1,4,2,'2022-03-04 14:42:26.197282');
INSERT INTO "businessDirectory_vendorbusinessrequest" VALUES (6,'Ogadi Nite Club',1,1,5,12,'2022-03-08 10:16:45.910049');
INSERT INTO "businessDirectory_vendorbusinessrequest" VALUES (7,'M4 Academy',0,1,2,2,'2022-04-03 19:08:35.138655');
INSERT INTO "businessDirectory_vendorbusinessrequest" VALUES (8,'Dyneco Refinery',1,1,3,13,'2022-10-14 14:50:16.309695');
INSERT INTO "businessDirectory_notification" VALUES (1,'Welcome','Dear Miracle,
Congratulation for joining us at UNNConnect. Our aim is to bridge the gap between vendors and students around the campus community.
Welcome onboard!!!',2,'2022-02-27 14:02:03.580841',0);
INSERT INTO "businessDirectory_notification" VALUES (2,'Disapproval of Proposed Business','Dear OgadiThis is to notify you that your business title Egodinedi was declined, appologies for any inconvinience.
 Signed
Admin.',12,'2022-03-02 15:17:43.454263',0);
INSERT INTO "businessDirectory_notification" VALUES (3,'Disapproval of Proposed Business','Dear MiracleThis is to notify you that your business title Another Business was declined, appologies for any inconvinience.
 Signed
Admin.',2,'2022-03-02 16:17:08.877766',0);
INSERT INTO "businessDirectory_notification" VALUES (4,'Disapproval of Proposed Business','Dear OgadiThis is to notify you that your business title Ogadinma was declined, appologies for any inconvinience.
 Signed
Admin.',12,'2022-03-02 16:17:56.654000',0);
INSERT INTO "businessDirectory_notification" VALUES (5,'Approval of Proposed Business','Dear Miracle,
this is to notify you that your business title Prosquino Ltd has been approved.
 Kindly Add all the necessary details as soon as possible.
 Signed
Admin.',2,'2022-03-04 14:43:12.452520',0);
INSERT INTO "businessDirectory_notification" VALUES (6,'Approval of Proposed Business','Dear Ogadi,
this is to notify you that your business title Ogadi Nite Club has been approved.
 Kindly Add all the necessary details as soon as possible.
 Signed
Admin.',12,'2022-03-08 10:17:26.206263',0);
INSERT INTO "businessDirectory_notification" VALUES (7,'Approval of Proposed Business','Dear prince,
this is to notify you that your business title Dyneco Refinery has been approved.
 Kindly Add all the necessary details as soon as possible.
 Signed
Admin.',13,'2022-10-14 14:51:05.829183',0);
INSERT INTO "businessDirectory_customermessage" VALUES (1,'I love your style...Keep it up.','2022-02-27 12:49:49.749145',2,0);
INSERT INTO "businessDirectory_customermessage" VALUES (2,'Nnna hey, you guys need to improve your services o.','2022-03-08 10:22:35.354012',12,0);
INSERT INTO "businessDirectory_user" VALUES (1,'pbkdf2_sha256$216000$vDAnUN0Io5z3$ZOsQGqXrjsn+DxwaeQ//t8F3Oh52QZp7RSItzC0uxi8=','2022-10-14 14:50:46.492066',1,'admin','Admin','-','admin@admin.com',1,1,'2022-02-26 00:46:35.673109',1,0,0,'','static/uploads/profile_photos/nophoto-male.jpg');
INSERT INTO "businessDirectory_user" VALUES (2,'pbkdf2_sha256$216000$4RSz1p8AHR8r$vZPXlne+3DHesuJ0Mtlx03Li/Dv86MYER4ofL3n/S0c=','2022-04-03 19:03:13.441117',0,'miraboy13','Miracle','Adolphus','miraboy13@gmail.com',0,1,'2022-02-26 00:58:44.349691',0,1,0,'08026889782','static/uploads/profile_photos/IMG_20210221_083301_941.jpg');
INSERT INTO "businessDirectory_user" VALUES (7,'pbkdf2_sha256$216000$rWIlfY4XOtnY$dqbtke47F7CUbb2p0e9AeTnLZ4YkmvlXrUpsNy0gIeU=','2022-03-07 16:36:23.103775',0,'ndubia','Lucy','Ndubia','lucy@gmail.com',0,1,'2022-02-26 02:43:01.390415',0,0,1,'08123456789','static/uploads/profile_photos/1597487050443.jpg');
INSERT INTO "businessDirectory_user" VALUES (8,'pbkdf2_sha256$216000$AJtiEX2jSmDU$50mDri43M9OpE6DIy6SqvFlh/I69OQ877adWLEmcXC4=','2022-03-08 10:22:00.764879',0,'admirashi','Gerald','Ekejuiba','geraldekejuiba@gmail.com',0,1,'2022-02-27 14:56:09.971954',0,0,1,'09015454578','static/uploads/profile_photos/IMG_20190310_100553_-_Copy.jpg');
INSERT INTO "businessDirectory_user" VALUES (9,'pbkdf2_sha256$216000$OhoBaeo6YpKb$ApnwItmS+uwqtdh0Vb/x3Oi9w8zf2qHSidqoVrAq/G0=','2022-03-04 14:47:05.090493',0,'davido','David','Ade','david@hotmail.com',0,1,'2022-02-28 10:10:01.293131',0,0,1,'08081234567','static/uploads/profile_photos/result580694_ghS8hYX.jpg');
INSERT INTO "businessDirectory_user" VALUES (10,'pbkdf2_sha256$216000$nI2puyFfOdAD$feaYdCSpHyBAfVsghxwl3ksMdrKW+r6GzsYdCzfjmYk=',NULL,0,'friday','Friday','Today','a@b.com',0,1,'2022-03-01 13:38:09.971782',0,0,1,'02020','static/uploads/profile_photos/nophoto-male.jpg');
INSERT INTO "businessDirectory_user" VALUES (11,'pbkdf2_sha256$216000$pG7lZyBh7Q8p$Mdl1Zh2UesnUjB+4zIaavLgXhlWVzrL2iiTBQETiE7k=',NULL,0,'sweet','swett','sew','a@2.com',0,1,'2022-03-01 13:40:36.709263',0,0,1,'0808','static/uploads/profile_photos/nophoto-male.jpg');
INSERT INTO "businessDirectory_user" VALUES (12,'pbkdf2_sha256$216000$rTDtPMZEE7Zw$yce+Pym2Rz4t5ppO6LvR1j/71bLmy1Pyw95zRsZ8ppk=','2022-03-08 10:09:14.844411',0,'ogadi','Ogadi','Okoro','ogadi@okoro.com',0,1,'2022-03-01 13:46:16.941938',0,1,0,'0502104215','static/uploads/profile_photos/nophoto-male.jpg');
INSERT INTO "businessDirectory_user" VALUES (13,'pbkdf2_sha256$216000$ZQX02raiEZUQ$jFYkLkVHzlXKUxGiy1SL4iGm9F+oVaxP4gqJKO35uC4=','2022-10-14 14:48:47.952367',0,'prince','prince','chima','prince.chima@gmail.com',0,1,'2022-10-14 14:48:40.764083',0,1,0,'0808080808','static/uploads/profile_photos/nophoto-male.jpg');
INSERT INTO "businessDirectory_user" VALUES (14,'pbkdf2_sha256$216000$N6Ct4s29AsUC$AY4EkGM8ToOMyut5tEnnSzZ5A27ulNbYztfP/FYSDwE=','2022-10-14 15:13:24.998098',0,'customer2','peter','edoka','p@eter.com',0,1,'2022-10-14 15:12:37.975844',0,0,1,'0808080808','static/uploads/profile_photos/nophoto-male.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (4,1,'static/uploads/images/clas_1_QBV45ar.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (5,1,'static/uploads/images/computer_1_lWykKNs.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (6,1,'static/uploads/images/m4_acadrmy.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (10,1,'static/uploads/images/dpetersf.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (11,10,'static/uploads/images/Untitled-1.png');
INSERT INTO "businessDirectory_uploads" VALUES (12,10,'static/uploads/images/dpetersf_DqBXlQs.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (13,6,'static/uploads/images/images_2.png');
INSERT INTO "businessDirectory_uploads" VALUES (14,6,'static/uploads/images/images_17.jpeg');
INSERT INTO "businessDirectory_uploads" VALUES (15,6,'static/uploads/images/images_13.jpeg');
INSERT INTO "businessDirectory_uploads" VALUES (16,11,'static/uploads/images/3601132112_8d00490483_b.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (18,11,'static/uploads/images/monica_copy_PymT3Wa.png');
INSERT INTO "businessDirectory_uploads" VALUES (19,11,'static/uploads/images/night_club1_BzMRPPb.jpg');
INSERT INTO "businessDirectory_uploads" VALUES (20,12,'static/uploads/images/printf_1.png');
INSERT INTO "businessDirectory_uploads" VALUES (21,12,'static/uploads/images/slack.png');
INSERT INTO "businessDirectory_category" VALUES (1,'Graphic Designs','static/uploads/thumbs/graphics_1.jpg');
INSERT INTO "businessDirectory_category" VALUES (2,'Computer Services','static/uploads/thumbs/computer_1.jpg');
INSERT INTO "businessDirectory_category" VALUES (3,'Mashia Spot','static/uploads/thumbs/maishai_1.jpg');
INSERT INTO "businessDirectory_category" VALUES (4,'Cakes & Pastries','static/uploads/thumbs/cake_1.jpg');
INSERT INTO "businessDirectory_category" VALUES (5,'Clubs','static/uploads/thumbs/night_club11_umQsEnw.jpg');
INSERT INTO "businessDirectory_category" VALUES (7,'Tutorial Masters','static/uploads/thumbs/clas_1.jpg');
INSERT INTO "businessDirectory_category" VALUES (8,'Fast Food','static/uploads/thumbs/restaurant2_5hiireL.jpg');
INSERT INTO "businessDirectory_category" VALUES (11,'POS Outlets','static/uploads/thumbs/images_17.jpeg');
INSERT INTO "businessDirectory_customersavedlisting" VALUES (1,'2022-02-27 13:01:56.694744',1,7);
INSERT INTO "businessDirectory_customersavedlisting" VALUES (5,'2022-03-01 14:23:00.397158',1,8);
INSERT INTO "businessDirectory_customersavedlisting" VALUES (6,'2022-03-04 14:47:19.478953',10,9);
INSERT INTO "businessDirectory_customersavedlisting" VALUES (7,'2022-03-04 14:47:26.895829',6,9);
INSERT INTO "businessDirectory_customersavedlisting" VALUES (8,'2022-10-14 15:13:38.685522',12,14);
INSERT INTO "businessDirectory_review" VALUES (1,5,'Miracle is very good!','2022-02-27 11:47:11.758421',1,7);
INSERT INTO "businessDirectory_review" VALUES (2,4,'This is a test review','2022-02-27 12:29:29.343757',1,7);
INSERT INTO "businessDirectory_review" VALUES (3,3,'Another test review','2022-02-27 12:29:44.732348',1,7);
INSERT INTO "businessDirectory_review" VALUES (4,0,'','2022-02-27 12:29:58.307948',1,7);
INSERT INTO "businessDirectory_review" VALUES (6,1,'Poor Services!!!!!','2022-02-27 22:46:42.996667',1,8);
INSERT INTO "businessDirectory_review" VALUES (7,3,'Yeah...average rating','2022-02-27 22:50:57.601529',1,8);
INSERT INTO "businessDirectory_review" VALUES (9,3,'This business is bay!!!!','2022-03-04 14:47:42.169929',6,9);
INSERT INTO "businessDirectory_review" VALUES (10,2,'You have a lot of things to work on','2022-03-08 10:22:52.081097',11,8);
INSERT INTO "businessDirectory_review" VALUES (11,5,'This place is super cool','2022-10-14 15:14:02.412142',12,14);
INSERT INTO "businessDirectory_campus" VALUES (1,'UNN');
INSERT INTO "businessDirectory_campus" VALUES (2,'UNEC');
CREATE INDEX IF NOT EXISTS "businessDirectory_business_owner_id_7a8768ae" ON "businessDirectory_business" (
	"owner_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_business_location_id_566308ab" ON "businessDirectory_business" (
	"location_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_business_category_id_028f1358" ON "businessDirectory_business" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_vendorbusinessrequest_vendor_id_51e783b2" ON "businessDirectory_vendorbusinessrequest" (
	"vendor_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_vendorbusinessrequest_category_id_750931bf" ON "businessDirectory_vendorbusinessrequest" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_vendorbusinessrequest_campus_id_990b6707" ON "businessDirectory_vendorbusinessrequest" (
	"campus_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_notification_receiver_id_767f90ac" ON "businessDirectory_notification" (
	"receiver_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_customermessage_receiver_id_29dc1285" ON "businessDirectory_customermessage" (
	"receiver_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_uploads_business_id_1e5d4db7" ON "businessDirectory_uploads" (
	"business_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_customersavedlisting_customer_id_aba26fdb" ON "businessDirectory_customersavedlisting" (
	"customer_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_customersavedlisting_business_id_ffa47edc" ON "businessDirectory_customersavedlisting" (
	"business_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_review_customer_id_4595810d" ON "businessDirectory_review" (
	"customer_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_review_business_id_1a45c7f7" ON "businessDirectory_review" (
	"business_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_user_user_permissions_permission_id_41e27918" ON "businessDirectory_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_user_user_permissions_user_id_6716143b" ON "businessDirectory_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "businessDirectory_user_user_permissions_user_id_permission_id_32ff0d59_uniq" ON "businessDirectory_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_user_groups_group_id_b52eb129" ON "businessDirectory_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "businessDirectory_user_groups_user_id_deb67316" ON "businessDirectory_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "businessDirectory_user_groups_user_id_group_id_68560f3c_uniq" ON "businessDirectory_user_groups" (
	"user_id",
	"group_id"
);
COMMIT;
