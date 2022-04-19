CREATE SEQUENCE IF NOT EXISTS public.order_sale_sale_line_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1 ;

ALTER SEQUENCE public.order_sale_sale_line_id_seq
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS public.order_sale
(
    sale_line_id integer NOT NULL DEFAULT nextval('order_sale_sale_line_id_seq'::regclass),
    order_num character varying(30) COLLATE pg_catalog."default",
    order_date timestamp without time zone,
    group_name character varying(50) COLLATE pg_catalog."default",
    car character varying(30) COLLATE pg_catalog."default",
    ticket character varying(20) COLLATE pg_catalog."default",
    sale_num character varying(20) COLLATE pg_catalog."default",
    sale_line_num character varying(5) COLLATE pg_catalog."default",
    item_no character varying(50) COLLATE pg_catalog."default",
    qty integer,
    amt integer,
    CONSTRAINT order_sale_pkey PRIMARY KEY (sale_line_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.order_sale
    OWNER to postgres;