.open "E74_GROUPS";

CREATE TABLE "E21_PERSON" (
  "id" VARCHAR(42),
  "surname" VARCHAR(42),
  "forename" VARCHAR(42),
  "addname" VARCHAR(42),
  "id_1" VARCHAR(42),
  "id_2" VARCHAR(42),
  "id_3" VARCHAR(42),
  "id_4" VARCHAR(42),
  "page" VARCHAR(42),
  "column" VARCHAR(42),
  "line" VARCHAR(42),
  "quote" VARCHAR(42),
  "date" VARCHAR(42),
  PRIMARY KEY ("id"),
  FOREIGN KEY ("id_3") REFERENCES "E74_GROUP" ("id"),
  FOREIGN KEY ("id_1") REFERENCES "E74_GROUP" ("id"),
  FOREIGN KEY ("id_2") REFERENCES "E74_GROUP" ("id"),
  FOREIGN KEY ("id_4") REFERENCES "E31_DOCUMENT" ("id")
);

CREATE TABLE "E31_DOCUMENT" (
  "id" VARCHAR(42),
  "quotation" VARCHAR(42),
  "storage_place" VARCHAR(42),
  "name" VARCHAR(42),
  PRIMARY KEY ("id")
);

CREATE TABLE "E74_GROUP" (
  "id" VARCHAR(42),
  "type" VARCHAR(42),
  "name" VARCHAR(42),
  PRIMARY KEY ("id")
);

CREATE TABLE "IS_PART_OF" (
  "id" VARCHAR(42),
  "id poele" VARCHAR(42),
  PRIMARY KEY ("id", "id poele"),
  FOREIGN KEY ("id") REFERENCES "E74_GROUP" ("id"),
  FOREIGN KEY ("id poele") REFERENCES "E74_GROUP" ("id")
);