CREATE TABLE `Container` (
    `ID` int  NOT NULL ,
    `loadingDate` datetime  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `Readings` (
    `ID` int  NOT NULL ,
    `temp` decimal  NOT NULL ,
    `humid` decimal  NOT NULL ,
    `containerID` int  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

