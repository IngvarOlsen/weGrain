-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE `Silo` (
    `ID` int  NOT NULL ,
    `fullPercent` decimal  NOT NULL ,
    `reciverSignalPin` int  NOT NULL ,
    `loadingDate` datetime  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Person` (
    `ID` int  NOT NULL ,
    `Name` string  NOT NULL ,
    `Address` string  NOT NULL ,
    `ContactNumber` int  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Contents` (
    `ID` int  NOT NULL ,
    `SiloId` int  NOT NULL ,
    `PersonId` int  NOT NULL ,
    `ContentType` string  NOT NULL ,
    `contentWeight` decimal  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

ALTER TABLE `Contents` ADD CONSTRAINT `fk_Contents_SiloId` FOREIGN KEY(`SiloId`)
REFERENCES `Silo` (`ID`);

ALTER TABLE `Contents` ADD CONSTRAINT `fk_Contents_PersonId` FOREIGN KEY(`PersonId`)
REFERENCES `Person` (`ID`);

CREATE INDEX `idx_Person_Name`
ON `Person` (`Name`);

