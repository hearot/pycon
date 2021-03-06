import React, { AnchorHTMLAttributes } from 'react';
import { Box } from '../box';
import { ButtonVariant } from './types';
import {
  getBackgroundColor,
  getFontSize,
  getBorderColor,
  getBorder,
  getTextColor,
} from './utils';

type Props = {
  variant?: ButtonVariant;
  children: React.ReactNode;
};

const Base = Box.extend`
  transition: background-color ${props => props.theme.timings[0]}s ease-out,
    color ${props => props.theme.timings[0]}s ease-out;
  cursor: pointer;
  text-transform: uppercase;
  text-decoration: none;
  font-family: ${props => props.theme.fonts.button};
  display: inline-block;
`;

const button = (
  { variant, children, ...additionalProps }: Props,
  tagName: 'a' | 'button',
) => {
  const Component = Base.withComponent(tagName);

  return (
    <Component
      px={3}
      py={2}
      borderRadius={100}
      bg={getBackgroundColor(variant, false)}
      color={getTextColor(variant, false)}
      fontSize={getFontSize(variant)}
      borderColor={getBorderColor(variant)}
      border={getBorder(variant, false)}
      hover={{
        backgroundColor: getBackgroundColor(variant, true),
        color: getTextColor(variant, true),
      }}
      focus={{
        backgroundColor: getBackgroundColor(variant, true),
        color: getTextColor(variant, true),
      }}
      {...additionalProps}
    >
      {children}
    </Component>
  );
};

type ButtonLinkProps = Props & AnchorHTMLAttributes<HTMLAnchorElement>;

export const Button = (props: Props) => button(props, 'button');
export const ButtonLink = (props: ButtonLinkProps) => button(props, 'a');
