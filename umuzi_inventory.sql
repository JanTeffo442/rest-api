--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Ubuntu 12.2-2.pgdg19.10+1)
-- Dumped by pg_dump version 12.2 (Ubuntu 12.2-2.pgdg19.10+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: umuzi; Type: SCHEMA; Schema: -; Owner: user
--

CREATE SCHEMA umuzi;


ALTER SCHEMA umuzi OWNER TO "user";

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: computers; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.computers (
    id integer NOT NULL,
    hard_drive_type character varying(50),
    processor character varying(50),
    amount_of_ram character varying(30),
    maximum_ram character varying(50),
    hard_drive_space character varying(30),
    form_factor character varying(40)
);


ALTER TABLE public.computers OWNER TO "user";

--
-- Name: computers_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.computers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.computers_id_seq OWNER TO "user";

--
-- Name: computers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.computers_id_seq OWNED BY public.computers.id;


--
-- Name: computers id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.computers ALTER COLUMN id SET DEFAULT nextval('public.computers_id_seq'::regclass);


--
-- Data for Name: computers; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.computers (id, hard_drive_type, processor, amount_of_ram, maximum_ram, hard_drive_space, form_factor) FROM stdin;
2	SSD	Intel	2GB	8GB	500GB	mini
3	HDD	intel core i3	8GB	16GB	1TB	mini
1	HDD	Intel celeron	1GB	6GB	256GB	medium
4	HDD	Intel quad-core i5 3.0GHz	8GB	32GB	1TB	medium
6	SSD	Intel dual core i7 3.5GHz	4GB	8GB	500GB	mini
7	HDD	Core i9 Extreme Edition	8GB	64GB	250Gb	mini
\.


--
-- Name: computers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.computers_id_seq', 7, true);


--
-- Name: computers computers_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.computers
    ADD CONSTRAINT computers_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

GRANT USAGE ON SCHEMA public TO "user";


--
-- PostgreSQL database dump complete
--

