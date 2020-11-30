CREATE TABLE IF NOT EXISTS telegram.users (
    id                          INT PRIMARY KEY,
    is_bot                      BOOLEAN NOT NULL,
    first_name                  VARCHAR(255) NOT NULL,
    username                    VARCHAR(255) UNIQUE NOT NULL,
    last_name                   VARCHAR(255),
    language_code               INT NOT NULL,
    can_join_groups             BOOLEAN,
    can_read_all_group_messages BOOLEAN,
    supports_inline_queries     BOOLEAN,
    date_joined                 TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS telegram.chat (
    id                              INT PRIMARY KEY,
    "type"                          VARCHAR(255) NOT NULL,
    title                           VARCHAR(255),
    username                        VARCHAR(255) UNIQUE NOT NULL,
    first_name                      VARCHAR(255) NOT NULL,
    last_name                       VARCHAR(255),
    all_members_are_administrators  BOOLEAN,
    photo                           VARCHAR(255),
    "description"                   TEXT,
    invite_link                     VARCHAR,
    pinned_message                  VARCHAR,
    "permissions"                   VARCHAR,
    slow_mode_delay                 VARCHAR,
    sticker_set_name                VARCHAR,
    can_set_sticker_set             BOOLEAN
);
